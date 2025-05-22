from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list():
    event = {
        "dog_id": "Leia",
        "timestamp": "2025-05-22T12:00:00Z",
        "x": 123.4,
        "y": 456.7,
    }
    resp = client.post("/api/v1/events/", json=event)
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == 1

    resp2 = client.get("/api/v1/events/")
    assert len(resp2.json()) == 1