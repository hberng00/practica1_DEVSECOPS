import pytest
import json
from app import app  # Asegurate de que el archivo de la app se llame app.py o ajusta el import.

@pytest.fixture
def client():
    """Fixture para configurar un cliente de prueba de Flask."""
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Prueba la ruta principal."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, CI/CD with Docker!' in response.data

def test_about(client):
    """Prueba la ruta /about."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.' in response.data

def test_greet(client):
    """Prueba la ruta /greet/<name>."""
    name = "TestUser"
    response = client.get(f'/greet/{name}')
    assert response.status_code == 200
    assert f'Hello, {name}!'.encode() in response.data

def test_add_valid(client):
    """Prueba la ruta /add con datos validos."""
    response = client.post('/add', json={"a": 10, "b": 20})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 30

def test_add_missing_data(client):
    """Prueba la ruta /add con datos faltantes."""
    response = client.post('/add', json={"a": 10})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_add_invalid_data(client):
    """Prueba la ruta /add con datos no numericos."""
    response = client.post('/add', json={"a": "foo", "b": "bar"})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data

def test_404_error(client):
    """Prueba la gestion de errores 404."""
    response = client.get('/nonexistent')
    assert response.status_cod
