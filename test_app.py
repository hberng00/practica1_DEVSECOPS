"""
Este módulo contiene pruebas para la aplicación Flask utilizando pytest.
Las pruebas verifican las rutas y el manejo de errores.
"""
import pytest
from app import app

@pytest.fixture(name="test_client")
def first_test_client():
    """
    Fixture que proporciona un cliente de prueba para la aplicación Flask.
    Este cliente simula peticiones HTTP para realizar las pruebas.
    """
    with app.test_client() as client:
        yield client

def test_home(test_client):
    """
    Test para la ruta principal ("/").
    Verifica que se recibe un mensaje de saludo correcto.
    """
    response = test_client.get('/')
    assert b'Hello, CI/CD with Docker!' in response.data

def test_about(test_client):
    """
    Test para la ruta "/about".
    Verifica que se recibe la información sobre la aplicación.
    """
    response = test_client.get('/about')
    assert b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.' in response.data

def test_greet(test_client):
    """
    Test para la ruta "/greet/<name>".
    Verifica que se reciba un saludo personalizado cuando se pasa un nombre en la URL.
    """
    name = 'John'
    response = test_client.get(f'/greet/{name}')
    assert f'Hello, {name}!'.encode() in response.data

def test_404_error(test_client):
    """
    Test para la ruta desconocida que lanza un error 404.
    Verifica que se maneje correctamente el error 404.
    """
    response = test_client.get('/nonexistent')
    assert response.status_code == 404
