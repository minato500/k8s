from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "App is running smoothly."}

def test_api_route():
    response = client.get("/api/v1/data")
    assert response.status_code == 200
    assert "data" in response.json()

def test_admin_route():
    response = client.get("/admin/status")
    assert response.status_code == 200
    assert "db_connection_user" in response.json()
