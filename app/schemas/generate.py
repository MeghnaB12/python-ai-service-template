"""Schemas for the example generation endpoint."""

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Input for a text-generation request."""

    prompt: str = Field(..., min_length=1, max_length=8000)
    max_tokens: int = Field(default=256, ge=1, le=4096)


class GenerateResponse(BaseModel):
    """Output of a text-generation request."""

    model: str
    completion: str
    prompt_tokens: int
    completion_tokens: int
