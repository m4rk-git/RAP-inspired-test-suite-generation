import os
import subprocess
import shutil
import sys
import csv
import time
from pathlib import Path

# CONFIGURATION
TARGET_DIR_REL = "data/temp"
TIME_BUDGET = 500
NUM_RUNS = 5


def get_paths():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    base_output_dir = os.path.join(script_dir, "results", "pynguin")
    return project_root, base_output_dir


def find_module_name(rel_path):
    p = Path(rel_path)
    return str(p.with_suffix("")).replace(os.sep, ".")


def run_pynguin(project_root, temp_output_dir, module_name):
    """
    Runs Pynguin into a temporary directory.
    """

    if os.path.exists(temp_output_dir):
        shutil.rmtree(temp_output_dir)
    os.makedirs(temp_output_dir)

    cmd = [
        "pynguin",
        f"--project-path={project_root}",
        f"--output-path={temp_output_dir}",
        f"--module-name={module_name}",
        "--algorithm=DYNAMOSA",
        "--maximum-search-time",
        str(TIME_BUDGET),
        "-v",
    ]

    env = os.environ.copy()
    env["PYTHONPATH"] = f"{project_root}:{env.get('PYTHONPATH', '')}"
    env["PYNGUIN_DANGER_AWARE"] = "true"

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, env=env, timeout=TIME_BUDGET + 30
        )

        if result.returncode != 0:
            print(f"Pynguin Failed {result.returncode}")
            return None

    except subprocess.TimeoutExpired:
        print("Pynguin timed out.")

    safe_name = "test_" + module_name.replace(".", "_") + ".py"
    generated_file = os.path.join(temp_output_dir, safe_name)

    if os.path.exists(generated_file):
        return generated_file

    # Fallback search
    found = list(Path(temp_output_dir).glob("test_*.py"))
    if found:
        return str(found[0])

    return None


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
    project_root, base_output_dir = get_paths()
    abs_target_dir = os.path.join(project_root, TARGET_DIR_REL)

    if not os.path.exists(base_output_dir):
        os.makedirs(base_output_dir)
    print(f"📁 Output Directory: {base_output_dir}")

    # 2. Init CSV
    csv_file = os.path.join(base_output_dir, "results.csv")
    csv_columns = ["Filename", "Run_ID", "Coverage", "Time(s)"]

    if not os.path.exists(csv_file):
        with open(csv_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()

    # 3. Check Input Directory
    if not os.path.exists(abs_target_dir):
        print(f"Target directory not found: {abs_target_dir}")
        sys.exit(1)

    if not os.path.exists(os.path.join(abs_target_dir, "__init__.py")):
        with open(os.path.join(abs_target_dir, "__init__.py"), "w") as f:
            pass

    all_files = [
        f
        for f in os.listdir(abs_target_dir)
        if f.endswith(".py") and f != "__init__.py" and not f.startswith("test_")
    ]

    print(f"Found {len(all_files)}")

    for filename in sorted(all_files):
        print(f"Processing: {filename}")

        file_rel_path = os.path.join(TARGET_DIR_REL, filename)
        abs_source_path = os.path.join(abs_target_dir, filename)
        module_name = find_module_name(file_rel_path)
        file_stem = Path(filename).stem

        for run_idx in range(1, NUM_RUNS + 1):
            print(f"\n--- Run {run_idx}/{NUM_RUNS} for {filename} ---")

            # Define final filename: test_example1_run1.py
            safe_name = f"test_{file_stem}_run{run_idx}.py"
            final_path = os.path.join(base_output_dir, safe_name)

            if os.path.exists(final_path):
                print(f"Result exists ({safe_name})")
                continue

            temp_worker_dir = os.path.join(
                base_output_dir, f".temp_{file_stem}_run{run_idx}"
            )

            start_time = time.time()

            generated_temp_path = run_pynguin(
                project_root, temp_worker_dir, module_name
            )

            elapsed_time = time.time() - start_time

            current_cov = 0.0

            if generated_temp_path:
                shutil.move(generated_temp_path, final_path)
                print(f"Generated: {safe_name}")
                print(f"Time: {elapsed_time:.2f}s")

                # Measure
                current_cov = measure_coverage(
                    final_path, abs_source_path, project_root
                )
                print(f"Coverage: {current_cov:.2f}%")
            else:
                print("Failed to generate tests.")
                current_cov = 0.0

            if os.path.exists(temp_worker_dir):
                shutil.rmtree(temp_worker_dir)

            # Save to CSV
            row_data = {
                "Filename": filename,
                "Run_ID": run_idx,
                "Coverage": f"{current_cov:.2f}",
                "Time(s)": f"{elapsed_time:.2f}",
            }

            try:
                with open(csv_file, "a", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=csv_columns)
                    writer.writerow(row_data)
            except Exception as e:
                print(f"Error appending to CSV: {e}")

    print("All runs completed. Results saved.")


if __name__ == "__main__":
    process_all_files()
