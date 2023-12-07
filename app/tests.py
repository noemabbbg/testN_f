from httpx import AsyncClient
import pytest
from app.main import app  # Импортируйте ваше FastAPI приложение

@pytest.mark.asyncio
async def test_create_rating():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/ratings/", json={"comic_id": 1, "user_id": 1, "value": 5})
    assert response.status_code == 200
    assert response.json() == {"comic_id": 1, "user_id": 1, "value": 5, "id": 1}

@pytest.mark.asyncio
async def test_get_comic_rating():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/comics/1/rating/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Comic Title", "author": "Author", "rating": 5.0}
