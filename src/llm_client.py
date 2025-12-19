import os
from typing import List, Optional, Union

try:
    from vllm import LLM, SamplingParams

    VLLM_AVAILABLE = True
except ImportError:
    VLLM_AVAILABLE = False
    print("Warning: vLLM not found. Install with 'pip install vllm'")


class VLLMDirectClient:
    """
    Directly loads the vLLM engine into this Python process.
    """

    def __init__(
        self,
        model_name: str = "",
        gpu_memory_utilization: float = 0.85,
        max_model_len: Optional[int] = None,
        enforce_eager: bool = False,
        kv_cache_dtype: str = "auto",
    ):
        if not VLLM_AVAILABLE:
            raise ImportError(
                "vLLM is not installed. Please install it to use direct inference."
            )

        print(f"Loading {model_name} directly into VRAM...")

        init_kwargs = {
            "model": model_name,
            "gpu_memory_utilization": gpu_memory_utilization,
            "dtype": "auto",
            "trust_remote_code": True,
            "tensor_parallel_size": 1,
            "enforce_eager": enforce_eager,
            "kv_cache_dtype": kv_cache_dtype,
        }

        if max_model_len is not None:
            init_kwargs["max_model_len"] = max_model_len

        self.llm = LLM(**init_kwargs)
        self.tokenizer = self.llm.get_tokenizer()

    def generate(
        self,
        prompt: Union[str, List[str]],
        temperature: float = 0.2,
        max_tokens: int = 512,
        n: int = 1,
        stop: Optional[List[str]] = None,
    ) -> List[str]:
        sampling_params = SamplingParams(
            temperature=temperature,
            max_tokens=max_tokens,
            n=n,
            stop=stop if stop else [],
        )

        prompts = [prompt] if isinstance(prompt, str) else prompt

        outputs = self.llm.generate(prompts, sampling_params, use_tqdm=False)

        result_texts = []
        for output in outputs:
            for completion in output.outputs:
                result_texts.append(completion.text)

        return result_texts
