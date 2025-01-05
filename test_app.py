import json
import pytest
from app import app

@pytest.fixture
def client():
    """Fixture para configurar un cliente de prueba de Flask."""
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.mark.usefixtures("client")
def test_home(client):
    """Prueba la ruta principal."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, CI/CD with Docker!' in response.data

@pytest.mark.usefixtures("client")
def test_about(client):
    """Prueba la ruta /about."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.' in response.data

@pytest.mark.usefixtures("client")
def test_greet(client):
    """Prueba la ruta /greet/<name>."""
    name = "TestUser"
    response = client.get(f'/greet/{name}')
    assert response.status_code == 200
    assert f'Hello, {name}! Bienvenido a nuestra aplicacion.'.encode() in response.data

@pytest.mark.usefixtures("client")
def test_add_valid(client):
    """Prueba la ruta /add con datos validos."""
    response = client.post('/add', json={"a": 10, "b": 20})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['result'] == 30

@pytest.mark.usefixtures("client")
def test_add_missing_data(client):
    """Prueba la ruta /add con datos faltantes."""
    response = client.post('/add', json={"a": 10})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == "Debes proporcionar los numeros 'a' y 'b'"

@pytest.mark.usefixtures("client")
def test_add_invalid_data(client):
    """Prueba la ruta /add con datos no numericos."""
    response = client.post('/add', json={"a": "foo", "b": "bar"})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == "Los valores 'a' y 'b' deben ser numeros"

@pytest.mark.usefixtures("client")
def test_404_error(client):
    """Prueba la gestion de errores 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == "La pagina no fue encontrada"

@pytest.mark.usefixtures("client")
def test_500_error(client):
    """Prueba la gestion de errores 500 forzando un fallo."""
    @app.route('/cause500')
    def cause500():
        raise ValueError("Forzar error 500")

    response = client.get('/cause500')
    assert response.status_code == 500
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == "Error interno del servidor"
