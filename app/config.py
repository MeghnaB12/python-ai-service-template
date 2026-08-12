"""Application settings loaded from environment / .env."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed application configuration.

    Values are read from environment variables (case-insensitive) or a local
    .env file. Add new settings here as your service grows.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "python-ai-service-template"
    environment: str = "local"
    log_level: str = "INFO"

    # Provider config - a concrete project fills these in.
    llm_provider: str = "stub"
    llm_api_key: str = ""
    llm_model: str = "stub-model"


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance (read the environment only once)."""
    return Settings()
