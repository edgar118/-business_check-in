import pytest
from fastapi.testclient import TestClient
from main import app  # Importa tu aplicación FastAPI

client = TestClient(app)

def test_create_user_type():
    # Define el payload para la solicitud POST
    payload = {"name": "Admin"}

    # Envía la solicitud POST al endpoint
    response = client.post("/user/type", json=payload)

    # Verifica que la respuesta tenga un código de estado 200
    assert response.status_code == 200

    # Verifica que el tipo de usuario se haya creado correctamente
    data = response.json()
    assert data["msg"] == "User type created"
    assert data["user_type"]["name"] == "Admin"
