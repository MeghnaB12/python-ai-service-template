"""FastAPI dependency providers."""

from functools import lru_cache

from app.config import get_settings
from app.llm import LLMClient, StubLLMClient


@lru_cache
def get_llm_client() -> LLMClient:
    """Provide the configured LLM client.

    Branch on settings.llm_provider here when you add real providers.
    """
    settings = get_settings()
    return StubLLMClient(model=settings.llm_model)
