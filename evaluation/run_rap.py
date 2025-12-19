import os
import sys
import shutil
import csv
import time
import subprocess
from pathlib import Path

# CONFIGURATION
TARGET_DIR_REL = "data/temp"
OUTPUT_SUBDIR = "results/rap"
MODEL_NAME = "Qwen/Qwen2.5-Coder-7B-Instruct"

NUM_RUNS = 5
MCTS_ITERS = 20
MCTS_DEPTH = 8


def get_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    base_output_dir = os.path.join(script_dir, OUTPUT_SUBDIR)

    src_path = os.path.join(project_root, "src")
    if src_path not in sys.path:
        sys.path.append(src_path)

    return project_root, base_output_dir


def find_module_name(rel_path):
    p = Path(rel_path)
    return str(p.with_suffix("")).replace(os.sep, ".")


def measure_coverage(test_file, source_file_abs, project_root):
    work_dir = os.path.dirname(test_file)
    cov_file = os.path.join(work_dir, ".coverage")
    config_file = os.path.join(work_dir, ".coveragerc")

    with open(config_file, "w") as f:
        f.write(f"[run]\ndata_file = {cov_file}\n")

    cmd = ["coverage", "run", f"--rcfile={config_file}", "-m", "pytest", test_file]
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{project_root}:{env.get('PYTHONPATH', '')}"

    try:
        subprocess.run(
            cmd, cwd=work_dir, capture_output=True, text=True, env=env, timeout=15
        )

        if not os.path.exists(cov_file):
            return 0.0

        import coverage

        cov = coverage.Coverage(data_file=cov_file)
        cov.load()

        target_lines = set()
        for f in cov.get_data().measured_files():
            if os.path.abspath(f) == source_file_abs:
                target_lines = set(cov.get_data().lines(f))
                break

        analysis = cov.analysis2(source_file_abs)
        executable_lines = set(analysis[1])

        if not executable_lines:
            return 0.0

        valid_hits = target_lines.intersection(executable_lines)
        return (len(valid_hits) / len(executable_lines)) * 100

    except Exception:
        return 0.0


def process_all_files():
    project_root, output_dir = get_paths()
    abs_target_dir = os.path.join(project_root, TARGET_DIR_REL)

    # 1. Init LLM
    try:
        from llm_client import VLLMDirectClient

        llm = VLLMDirectClient(
            model_name=MODEL_NAME, max_model_len=16384, gpu_memory_utilization=0.85
        )
    except Exception as e:
        print(f"Failed to load LLM: {e}")
        return

    # Import RAP components
    try:
        from world_model import CodeCoverageWorldModel
        from search_config import TestGenConfig
        from reasoners.algorithm import MCTS
    except ImportError as e:
        print(f"Failed to import RAP components from src/: {e}")
        return

    # 2. Prepare Output Directory
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"Output Directory: {output_dir}")

    # 3. Init CSV
    csv_file = os.path.join(output_dir, "results.csv")
    csv_columns = ["Filename", "Run_ID", "Coverage", "Time(s)"]

    # Only write header if file doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()

    # 4. Find Files
    if not os.path.exists(os.path.join(abs_target_dir, "__init__.py")):
        with open(os.path.join(abs_target_dir, "__init__.py"), "w") as f:
            pass

    all_files = [
        f
        for f in os.listdir(abs_target_dir)
        if f.endswith(".py") and f != "__init__.py" and not f.startswith("test_")
    ]

    print(f"{len(all_files)} files to test.")

    for filename in sorted(all_files):
        print(f"Processing File: {filename}")

        file_rel_path = os.path.join(TARGET_DIR_REL, filename)
        abs_source_path = os.path.join(abs_target_dir, filename)
        module_name = find_module_name(file_rel_path)
        file_stem = Path(filename).stem  # e.g. "example2"

        for run_idx in range(1, NUM_RUNS + 1):
            print(f"\n--- Run {run_idx}/{NUM_RUNS} for {filename} ---")

            safe_name = f"test_{file_stem}_run{run_idx}.py"
            final_output_path = os.path.join(output_dir, safe_name)

            # Check if this run already exists
            if os.path.exists(final_output_path):
                print(f"Result exists ({safe_name})")
                continue

            temp_work_dir = os.path.join(output_dir, f".temp_{file_stem}_run{run_idx}")
            if os.path.exists(temp_work_dir):
                shutil.rmtree(temp_work_dir)
            os.makedirs(temp_work_dir)

            start_time = time.time()
            success = False

            try:
                # Init World Model
                world_model = CodeCoverageWorldModel(
                    source_file_path=abs_source_path, work_dir=temp_work_dir
                )

                # Read source code
                with open(abs_source_path, "r") as f:
                    source_code = f.read()

                # Init Search Config
                search_config = TestGenConfig(
                    llm=llm, source_code=source_code, source_module_name=module_name
                )

                # Init & Run MCTS
                search_algo = MCTS(
                    output_trace_in_each_iter=False,
                    w_exp=1.0,
                    n_iters=MCTS_ITERS,
                    depth_limit=MCTS_DEPTH,
                )

                search_algo(world_model, search_config)

                # Save Best Result
                best_code = world_model.best_test_suite_code
                with open(final_output_path, "w") as f:
                    f.write(best_code)

                success = True

            except Exception as e:
                print(f"RAP MCTS Error: {e}")

            elapsed_time = time.time() - start_time

            # Clean up temp
            if os.path.exists(temp_work_dir):
                shutil.rmtree(temp_work_dir)

            # Measure & Save
            current_cov = 0.0
            if success and os.path.exists(final_output_path):
                print(f"Generated: {safe_name}")
                current_cov = measure_coverage(
                    final_output_path, abs_source_path, project_root
                )
                print(f"Coverage: {current_cov:.2f}%")
            else:
                print("Failed to generate tests.")

            row_data = {
                "Filename": filename,
                "Run_ID": run_idx,
                "Coverage": f"{current_cov:.2f}",
                "Time(s)": f"{elapsed_time:.2f}",
            }

            with open(csv_file, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=csv_columns)
                writer.writerow(row_data)

    print("All runs completed. Results saved.")


if __name__ == "__main__":
    process_all_files()
