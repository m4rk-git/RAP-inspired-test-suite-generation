import os
from reasoners.algorithm import MCTS
from world_model import CodeCoverageWorldModel
from search_config import TestGenConfig
from llm_client import VLLMDirectClient


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def main():
    source_file = "/root/RAPiT-project/data/assignment_tests/example1.py"
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    source_code = read_file(source_file)

    # model_name = "mistralai/Mistral-7B-Instruct-v0.2"
    # max_len = 8192

    model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
    max_len = 16384

    # model_name = "deepseek-ai/deepseek-coder-7b-instruct-v1.5"
    # max_len = 4096

    print(f"Initializing Direct vLLM Engine with {model_name} (Max Len: {max_len})...")

    llm = VLLMDirectClient(model_name=model_name, max_model_len=max_len)

    world_model = CodeCoverageWorldModel(source_file_path=source_file)

    search_config = TestGenConfig(
        llm=llm,
        source_code=source_code,
        source_module_name=world_model.source_module,
    )

    search_algo = MCTS(
        output_trace_in_each_iter=True, w_exp=1.0, n_iters=20, depth_limit=8
    )

    print("Starting RAP-Test Generation...")
    search_algo(world_model, search_config)

    print("\n" + "=" * 30)
    print("SEARCH COMPLETE")
    print(f"Highest Coverage: {world_model.best_coverage:.2f}%")
    print("\n=== BEST GENERATED TEST SUITE ===")
    print(world_model.best_test_suite_code)
    print("=" * 30)

    with open("/root/RAPiT-project/final_best_suite.py", "w") as f:
        f.write(world_model.best_test_suite_code)
    print("Saved best suite to 'final_best_suite.py'")


if __name__ == "__main__":
    main()
