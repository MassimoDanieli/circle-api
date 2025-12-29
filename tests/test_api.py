from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthz():
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"ok": True}


def test_circle_ok():
    r = client.get("/circle?radius=2&units=cm")
    assert r.status_code == 200
    data = r.json()
    assert data["radius"] == 2
    assert data["units"] == "cm"
    assert "area" in data and data["area"] > 0
    assert "circumference" in data and data["circumference"] > 0


def test_circle_requires_positive_radius():
    r = client.get("/circle?radius=0")
    assert r.status_code == 422

