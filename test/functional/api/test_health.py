import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_ok(client: AsyncClient):
    res = await client.get("/health")
    res.raise_for_status()

    data = res.json()
    assert data["status"] == "ok"
