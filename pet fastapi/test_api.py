from httpx import ASGITransport, AsyncClient, AsyncHTTPTransport
import pytest  
from pet_FastAPI import app
    
@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
        ) as client:
        response = await client.get("/")
        data = response.json()
        assert response.status_code == 200
        assert data == {"message": "Welcome to Pet FastAPI!"}