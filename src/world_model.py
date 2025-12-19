import os
import re
import subprocess
import coverage
import sys
from typing import Set, Tuple, Dict, NamedTuple, List
from reasoners import WorldModel
from pathlib import Path
import ast

def find_project_root(current_path: Path, marker_file: str = '.gitignore') -> Path:
    current_path = current_path.resolve()
    for parent in [current_path] + list(current_path.parents):
        if (parent / marker_file).exists():
            return parent
    return current_path

def path_to_import_string(file_path: Path, root_path: Path) -> str:
    try:
        relative_path = file_path.relative_to(root_path)
    except ValueError:
        return file_path.stem
    return str(relative_path.with_suffix('')).replace(os.sep, '.')


def get_imports(code):
    tree = ast.parse(code)
    imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.asname:
                    imports.append(f"import {alias.name} as {alias.asname}")
                else:
                    imports.append(f"import {alias.name}")
        
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ''
            if node.level > 0:
                module = "." * node.level + module
            
            for alias in node.names:
                if alias.asname:
                    imports.append(f"from {module} import {alias.name} as {alias.asname}")
                else:
                    imports.append(f"from {module} import {alias.name}")
                
    return imports

class TestingState(NamedTuple):
    test_cases: Tuple[str, ...]
    covered_lines: frozenset[int]
    missing_lines: frozenset[int]
    coverage_percent: float

class CodeCoverageWorldModel(WorldModel):
    def __init__(self, source_file_path: str, work_dir: str = "temp_workspace", dry_run: bool = False):
        self.source_file_path = os.path.abspath(source_file_path)
        self.work_dir = os.path.abspath(work_dir)
        self.dry_run = dry_run
        
        self.project_root = find_project_root(Path(source_file_path).parent)
        self.source_module = path_to_import_string(Path(source_file_path), self.project_root)

        source_code = open(self.source_file_path).read()
        self.import_lines = get_imports(source_code)
        
        os.makedirs(self.work_dir, exist_ok=True)
        self._init_environment()
        
        self.best_test_suite_code = f"import pytest\nimport {self.source_module}\n"
        self.best_coverage = -1.0
        self.best_covered_lines = set()

        self.initial_test_suite_code = None
        self.initial_coverage = -1.0

    def _init_environment(self):
        self.cov_file = os.path.join(self.work_dir, ".coverage")
        self.config_file = os.path.join(self.work_dir, ".coveragerc")
        with open(self.config_file, "w") as f:
            f.write(f"[run]\ndata_file = {self.cov_file}\n")

    def _get_all_executable_lines(self) -> Set[int]:
        cov = coverage.Coverage()
        try:
            analysis = cov.analysis2(self.source_file_path)
            return set(analysis[1])
        except Exception as e:
            print(f"[WARN] Could not analyze source file statically: {e}")
            return set()

    def init_state(self) -> TestingState:
        all_lines = self._get_all_executable_lines()
        return TestingState(test_cases=tuple(), covered_lines=frozenset(), missing_lines=frozenset(all_lines), coverage_percent=0.0)

    def step(self, state: TestingState, action: str) -> Tuple[TestingState, Dict]:
        print(f"Adding test case: {action[:40]}...")
        new_cases = state.test_cases + (action,)
        
        full_test_code = self._assemble_test_file(new_cases)
        test_file_path = os.path.join(self.work_dir, "test_generated.py")
        
        if not self.dry_run:
            with open(test_file_path, "w") as f:
                f.write(full_test_code)

        if self.dry_run:
            self.best_test_suite_code = full_test_code
            next_state = TestingState(
                test_cases=new_cases,
                covered_lines=state.covered_lines, 
                missing_lines=state.missing_lines, 
                coverage_percent=state.coverage_percent 
            )
            return next_state, {"status": "dry_run_added"}
        
        try:
            compile(full_test_code, 'test_string', 'exec')
        except SyntaxError as e:
            return state, {"status": "syntax_error", "error": str(e)}

        cmd = [
            "coverage", "run",
            f"--rcfile={self.config_file}",
            "-m", "pytest",
            test_file_path
        ]
        
        try:
            result = subprocess.run(
                cmd, 
                cwd=self.work_dir, 
                capture_output=True, 
                text=True, 
                timeout=5
            )
            
            if result.returncode != 0 and result.returncode != 1:
                print(f"[ERROR] Execution Failed!\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}")
                
        except subprocess.TimeoutError:
            return state, {"status": "timeout"}

        new_executed, new_missing, new_percent = self._get_coverage_data()
        
        if new_percent > self.best_coverage:
            print(f"[New Record] Coverage: {new_percent:.2f}% (Tests: {len(new_cases)})")
            self.best_coverage = new_percent
            self.best_test_suite_code = full_test_code
            self.best_covered_lines = new_executed

        next_state = TestingState(
            test_cases=new_cases,
            covered_lines=frozenset(new_executed),
            missing_lines=frozenset(new_missing),
            coverage_percent=new_percent
        )
        
        return next_state, {"newly_covered": len(new_executed) - len(state.covered_lines)}

    def _assemble_test_file(self, cases: Tuple[str, ...]) -> str:
        source_dir = os.path.dirname(self.source_file_path)
        
        target_mod = self.source_module
        
        lines = [
            "import sys",
            "import os",
            f"sys.path.append(r'{self.project_root}')",
            f"sys.path.append(r'{source_dir}')",
            "import pytest",
            f"import {target_mod} as {target_mod.split('.')[-1]}",
            f"from {target_mod} import *",
            ""
        ] + self.import_lines + [""]
        
        for i, code in enumerate(cases, 1):
            safe_module_name = self.source_module.replace(".", "_")
            new_name = f"test_{safe_module_name}_{i}"
            
            if "def test_" in code:
                code = re.sub(r"def\s+test_\w+\s*\(", f"def {new_name}(", code, count=1)
            else:
                code = f"def {new_name}():\n    " + code.replace("\n", "\n    ")
            
            lines.append(code)
            lines.append("") 
            
        return "\n".join(lines)

    def _get_coverage_data(self) -> Tuple[Set[int], Set[int], float]:
        if not os.path.exists(self.cov_file):
            return set(), set(), 0.0
            
        cov = coverage.Coverage(data_file=self.cov_file)
        cov.load()
        
        measured_files = cov.get_data().measured_files()
        target_abs = os.path.abspath(self.source_file_path)
        matching_file = None

        for f in measured_files:
            f_abs = os.path.abspath(f)
            if f_abs == target_abs:
                matching_file = f
                break
            if os.path.realpath(f) == os.path.realpath(self.source_file_path):
                matching_file = f
                break
            if f_abs.endswith(os.path.sep + os.path.basename(target_abs)):
                 matching_file = f
                 break

        if not matching_file:
            if measured_files:
                print(f"[DEBUG] Target {target_abs} NOT found in: {measured_files}")
            return set(), set(), 0.0

        try:
            analysis = cov.analysis2(matching_file)
            executable_lines = set(analysis[1])
            missing = set(analysis[3])
            executed = executable_lines - missing
            
            if not executable_lines:
                return set(), set(), 0.0
                
            percent = (len(executed) / len(executable_lines)) * 100
            return executed, missing, percent
        except Exception as e:
            print(f"[ERROR] Analysis failed: {e}")
            return set(), set(), 0.0

    def is_terminal(self, state: TestingState) -> bool:
        if state.coverage_percent >= 100.0:
            return True
        return False