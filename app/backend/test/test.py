import pytest
from fastapi.testclient import TestClient
from main import app  # Importa tu aplicación FastAPI

#docker exec -it prueba_big-api-1 /bin/bash

client = TestClient(app)

def test_get_user_type(client):
    response = client.get("/type")
    assert response.status_code == 200
    assert response.json() == [] 

def test_create_user_success(client):
    user_data = {
        "name": "John Doe",
        "role": 1,
        "document_id": 12345,
        "department_id": 1,
        "user_type_id": 1
    }
    response = client.post("/", json=user_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Created John Doe"}

def test_create_user_already_exists(client):
    user_data = {
        "name": "Jane Doe",
        "role": 1,
        "document_id": 12345,
        "department_id": 2,
        "user_type_id": 1
    }
    response = client.post("/", json=user_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "User already exist"}
