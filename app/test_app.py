import pytest
from unittest.mock import MagicMock, patch
import app as flask_app

@pytest.fixture
def client():
    flask_app.app.config["TESTING"] = True

    # 🔥 MOCK REDIS
    with patch("app.r") as mock_redis:
        mock_redis.incr.return_value = 1
        mock_redis.get.return_value = "1"

        with flask_app.app.test_client() as client:
            yield client

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200

def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
