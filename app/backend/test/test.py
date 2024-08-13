import pytest
from fastapi.testclient import TestClient
from main import app  # Importa tu aplicación FastAPI

client = TestClient(app)

def test_create_user_type():
    payload = {"name": "Admin"}
    response = client.post("/user/type", json=payload)

    assert response.status_code == 200
    
    data = response.json()
    assert data["msg"] == "User type created"
    assert data["user_type"]["name"] == "Admin"
