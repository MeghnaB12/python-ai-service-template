"""Example AI endpoint wired through the LLMClient dependency."""

from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_llm_client
from app.llm import LLMClient
from app.schemas.generate import GenerateRequest, GenerateResponse

router = APIRouter(prefix="/v1", tags=["generate"])


@router.post("/generate")
async def generate(
    request: GenerateRequest,
    client: Annotated[LLMClient, Depends(get_llm_client)],
) -> GenerateResponse:
    """Generate text for a prompt using the injected LLM client."""
    return await client.generate(request.prompt, request.max_tokens)
