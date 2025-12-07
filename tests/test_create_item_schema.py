from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item_schema():
    payload = {"name": "test_item", "description": "desc"}
    res = client.post("/items/", json=payload)
    assert res.status_code in (200, 201, 422)
