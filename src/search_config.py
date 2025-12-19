import re
from reasoners import SearchConfig
from typing import List, Tuple, Dict
from world_model import TestingState


class TestGenConfig(SearchConfig):
    def __init__(
        self, llm, source_code: str, source_module_name: str
    ):
        super().__init__()
        self.llm = llm
        self.source_code = source_code
        self.source_module_name = source_module_name

    def get_actions(self, state: TestingState) -> List[str]:
        prompt = self._construct_prompt(state)

        responses = self.llm.generate(
            prompt, n=3, temperature=0.8, stop=["```", "### Instruction", "<|EOT|>"]
        )

        valid_actions = []
        for i, r in enumerate(responses):

            clean_code = self._clean_llm_output(r)
            if not clean_code or len(clean_code) < 10:
                continue
            valid_actions.append(clean_code)

        if not valid_actions:
            valid_actions.append("def test_dummy_fallback():\n    pass")

        return valid_actions

    def _format_missing_lines(self, missing_lines: list) -> str:
        if not missing_lines:
            return "None"

        sorted_lines = sorted(list(missing_lines))
        ranges = []
        range_start = sorted_lines[0]
        prev = sorted_lines[0]

        for curr in sorted_lines[1:]:
            if curr == prev + 1:
                prev = curr
            else:
                if range_start == prev:
                    ranges.append(str(range_start))
                else:
                    ranges.append(f"{range_start}-{prev}")
                range_start = curr
                prev = curr

        if range_start == prev:
            ranges.append(str(range_start))
        else:
            ranges.append(f"{range_start}-{prev}")

        return ", ".join(ranges)

    def _add_line_numbers(self, source_code: str) -> str:
        lines = source_code.splitlines()
        numbered_lines = []
        for i, line in enumerate(lines, 1):
            numbered_lines.append(f"{i:4d} | {line}")
        return "\n".join(numbered_lines)

    def _clean_llm_output(self, raw_text: str) -> str:
        text = raw_text.strip()

        if "```python" in text:
            text = text.split("```python")[1]
        if "```" in text:
            text = text.split("```")[0]

        # lines = text.split('\n')
        # cleaned_lines = [line for line in lines if not line.strip().startswith("assert")]
        # text = "\n".join(cleaned_lines)

        text = text.strip()

        if not text.startswith("def test_"):
            if re.match(r"^\w+\s*\(", text):
                text = "def test_" + text
            else:
                text = "def test_generated_wrapper():\n    " + text.replace(
                    "\n", "\n    "
                )

        if "def test_" not in text and "def " in text:
            text = text[text.find("def ") :]

        return text

    def reward(self, state: TestingState, action: str, **kwargs) -> Tuple[float, Dict]:
        score = state.coverage_percent / 100.0
        print(f"   [Reward-Exec] Coverage: {state.coverage_percent:.1f}%")
        return score, {"type": "execution", "lines": len(state.covered_lines)}

    def _estimate_coverage_with_llm(self, state: TestingState) -> float:
        all_tests = "\n".join(state.test_cases)
        if not all_tests.strip():
            return 0.0

        prompt = f"""### Code:
{self.source_code}
### Tests:
{all_tests}
### Task:
Estimate the code coverage % (0-100) of these Tests on the Code.
Output ONLY the number.
"""
        try:

            resp = self.llm.generate(prompt, n=1, temperature=0.1, max_tokens=5)[0]

            match = re.search(r"(\d+(\.\d+)?)", resp)
            val = float(match.group(1)) if match else 0.0
            return max(0.0, min(val, 100.0))
        except Exception:
            return 0.0

    def _construct_prompt(self, state: TestingState) -> str:

        numbered_source = self._add_line_numbers(self.source_code)

        missing_str = self._format_missing_lines(list(state.missing_lines))

        prompt = f"""###
SOURCE_CODE ({self.source_module_name.split('.')[-1]}):
{numbered_source}

TARGET_MISSING_LINES (Focus on these lines!): {missing_str}

REQUIREMENTS:

Output ONLY valid Python code.

The code must be exactly ONE complete function starting with def.

Do NOT use markdown.
DO NOT use asserts because these will be automatically ignored.

Instruction:
You are a **Python Execution Path Solver**. Your ONLY goal is to generate exactly ONE PyTest test case that forces the Python interpreter to execute one line listed in 'TARGET_MISSING_LINES'.
Refer to data structures, classes and functions in the 'SOURCE_CODE' only with '{self.source_module_name.split('.')[-1]}'.
DO NOT EXPLAIN YOUR REASONING AT ALL.

Response:
def test_"""
        # print(prompt)
        # print(state.test_cases)
        return prompt
