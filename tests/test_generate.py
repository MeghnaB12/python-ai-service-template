"""Generation endpoint tests."""

from httpx import AsyncClient


async def test_generate_returns_completion(client: AsyncClient) -> None:
    response = await client.post("/v1/generate", json={"prompt": "hello world"})
    assert response.status_code == 200
    body = response.json()
    assert body["model"] == "stub-model"
    assert "stub completion" in body["completion"]


async def test_generate_rejects_empty_prompt(client: AsyncClient) -> None:
    response = await client.post("/v1/generate", json={"prompt": ""})
    assert response.status_code == 422
