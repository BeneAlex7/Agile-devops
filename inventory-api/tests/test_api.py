import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check_status(client):
    """Test que /health retourne 200"""
    response = client.get('/api/v1/health')
    assert response.status_code == 200
    assert response.json["status"] == "OK"

def test_list_servers(client):
    """Test que /servers retourne la liste"""
    response = client.get('/api/v1/servers')
    assert response.status_code == 200
    assert "servers" in response.json
    assert isinstance(response.json["servers"], list)
    assert response.json["count"] == 2

def test_get_server_success(client):
    """Test que /servers/1 retourne le bon serveur"""
    response = client.get('/api/v1/servers/1')
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert response.json["hostname"] == "web-prod-01"

def test_get_server_not_found(client):
    """Test que /servers/999 retourne 404"""
    response = client.get('/api/v1/servers/999')
    assert response.status_code == 404
    assert "error" in response.json
