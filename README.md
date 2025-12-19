# RAP-TestGen: Agentic Unit Test Generation

Adapts **Reasoning via Planning (RAP)** for Python testing by modeling generation as an MCTS search. It combines **Qwen2.5-Coder** with a deterministic execution environment to provide ground-truth coverage rewards. This feedback loop allows the agent to iteratively maximize coverage in complex files, outperforming zero-shot baselines.

## Methodology

This project implements the **RAP (Reasoning via Planning)** framework adapted for software testing.

**Reference:** This work is based on the paper:  
> **Reasoning with Language Model is Planning with World Model**: Shibo Hao, Yi Gu, Haodi Ma, Joshua J. Hong, Zhen Wang, Daisy Zhe Wang, Zhiting Hu.  
> *arXiv:2305.14992* (2023). [Link to Paper](https://arxiv.org/abs/2305.14992)

## Installation

1. **Clone the repository:**

   ``https://github.com/m4rk-git/RAP-inspired-test-suite-generation.git``


2. **Requirements:**

    ``pip install -r requirements.txt``

## How to Run
1. **Configure the Model:** Ensure model_name in ``mcts_driver`` has the wanted llm selected (default: Qwen/Qwen2.5-Coder-7B-Instruct).

2. **Change Target File:** Change the path to the target file in ``src/mcts_driver.py``

3. **Run the Search:** Run the search using ``python src/mcts_driver.py``

**View Results:** The generated test suite will be saved in the ``final_best_suite.py`` file

## Project Structure

- ``mcts_driver.py``: Main entry point controlling the MCTS loop.

- ``world_model.py``: Handles code compilation, execution (Pytest), and reward calculation (Coverage).

- ``llm_client.py``: Interface for VLLM to generate test candidates.

- ``search_config.py``: Defines the RAP actions, states, and prompt engineering logic.