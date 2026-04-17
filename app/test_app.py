import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
