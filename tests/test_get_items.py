from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_items_returns_list():
    res = client.get("/items/")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
