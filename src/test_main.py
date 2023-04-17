from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_articles():
    response = client.get("/article/")
    assert response.status_code == 200
    assert response.json() == {
        "response_code": 200,
        "status": "success",
        "message": "Articles retrieved",
        "data": None,
    }


def test_get_article_by_id():
    response = client.get("/article/1")
    assert response.status_code == 200
    assert response.json() == {
        "response_code": 200,
        "status": "success",
        "message": "Article retrieved",
        "data": None,
    }
