"""
Este módulo contiene pruebas para la aplicación Flask utilizando pytest.#-
Las pruebas verifican las rutas y el manejo de errores.#-
"""
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(test_client):
    response = test_client.get('/')
    assert b'Hello, CI/CD with Docker!' in response.data

def test_about(test_client):
    response = test_client.get('/about')
    assert b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.' in response.data

def test_greet(test_client):
    name = 'John'
    response = test_client.get(f'/greet/{name}')
    assert f'Hello, {name}!'.encode() in response.data

def test_add_valid(test_client):
    response = test_client.post('/add', json={'a': 10, 'b': 20})
    data = response.get_json()
    assert data['result'] == 30

def test_add_missing_data(test_client):
    response = test_client.post('/add', json={'a': 10})
    data = response.get_json()
    assert 'error' in data

def test_add_invalid_data(test_client):
    response = test_client.post('/add', json={'a': 'ten', 'b': 'twenty'})
    data = response.get_json()
    assert 'error' in data

def test_404_error(test_client):
    response = test_client.get('/nonexistent')
    assert response.status_code == 404
