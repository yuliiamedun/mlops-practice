from fastapi.testclient import TestClient
from mlops_practice.api import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_add():
    response = client.post("/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_divide_by_zero():
    response = client.post("/divide", json={"a": 1, "b": 0})
    assert response.status_code == 400
