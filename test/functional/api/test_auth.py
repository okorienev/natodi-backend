import pytest

from httpx import AsyncClient

from cli.app.commands.auth import generate_token
from app.settings import settings

@pytest.mark.asyncio
async def test_no_authorization_error(client: AsyncClient):
    res = await client.post("/files/authorization")

    assert res.status_code == 403
    assert res.json() == {
        "detail": "Not authenticated"
    }
 
@pytest.mark.asyncio
async def test_not_token_authorization_error(client: AsyncClient):
    res = await client.post("/files/authorization", headers={"Authorization": "Bearer 123"})
    
    assert res.status_code == 403

@pytest.mark.asyncio
async def test_invalid_token_authorization_error(client: AsyncClient):
    res = await client.post("/files/authorization", headers={"Authorization": "Bearer a123.b123.c123"})
    
    assert res.status_code == 403

@pytest.mark.asyncio
async def test_expired_authorization_error(client: AsyncClient):
    access_token = "Bearer " + generate_token(username="admin", expire_delta=-1, secret_key=settings.SECRET_KEY)
    print(access_token)
    res = await client.post("/files/authorization", headers={"Authorization": access_token})
    
    assert res.status_code == 403
    assert res.json() == {
        "detail": "Signature has expired."
    }

@pytest.mark.asyncio
async def test_wrong_credentials_authorization_error(client: AsyncClient):
    access_token = "Bearer " + generate_token(username="notadmin", expire_delta=1, secret_key=settings.SECRET_KEY)
    print(access_token)
    res = await client.post("/files/authorization", headers={"Authorization": access_token})
    
    assert res.status_code == 403
    assert res.json() == {
        "detail": "Could not validate credentials"
    }

@pytest.mark.asyncio
async def test_authorization_ok(client: AsyncClient):
    access_token = "Bearer " + generate_token(username="admin", expire_delta=1, secret_key=settings.SECRET_KEY)
    print(access_token)
    res = await client.post("/files/authorization", headers={"Authorization": access_token})
    
    assert res.status_code == 200

