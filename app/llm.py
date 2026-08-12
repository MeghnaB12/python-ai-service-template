"""LLM client abstraction.

The Protocol lets handlers depend on an interface, not a concrete provider.
Swap StubLLMClient for a real Anthropic/OpenAI client in a concrete project
without changing any route code.
"""

from typing import Protocol

from app.schemas.generate import GenerateResponse


class LLMClient(Protocol):
    """Minimal interface every provider client must satisfy."""

    async def generate(self, prompt: str, max_tokens: int) -> GenerateResponse: ...


class StubLLMClient:
    """Deterministic stand-in so the template runs with no API key."""

    def __init__(self, model: str) -> None:
        self._model = model

    async def generate(self, prompt: str, max_tokens: int) -> GenerateResponse:
        """Return a fake completion derived from the prompt."""
        completion = f"[stub completion for a prompt of {len(prompt)} chars]"
        return GenerateResponse(
            model=self._model,
            completion=completion,
            prompt_tokens=len(prompt.split()),
            completion_tokens=len(completion.split()),
        )
