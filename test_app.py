"""
Este módulo contiene pruebas para la aplicación Flask utilizando pytest.
Las pruebas verifican las rutas y el manejo de errores.
"""

import pytest
from app import app  # Asegúrate de que 'app' esté importado correctamente

@pytest.fixture
def client():
    """
    Fixture que proporciona un cliente de prueba para la aplicación Flask.
    """
    with app.test_client() as client:
        yield client

def test_home(client):
    """
    Test para la ruta principal ("/").
    Verifica que se recibe un mensaje de saludo correcto.
    """
    response = client.get('/')
    assert response.data == b'Hello, CI/CD with Docker!'
    assert response.status_code == 200

def test_about(client):
    """
    Test para la ruta "/about".
    Verifica que se recibe la información sobre la aplicación.
    """
    response = client.get('/about')
    assert response.data == b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.'
    assert response.status_code == 200

def test_greet(client):
    """
    Test para la ruta "/greet/<name>".
    Verifica que se reciba un saludo personalizado cuando se pasa un nombre en la URL.
    """
    response = client.get('/greet/John')
    assert response.data == b'Hello, John! Bienvenido a nuestra aplicacion.'
    assert response.status_code == 200

def test_page_not_found(client):
    """
    Test para la ruta desconocida que lanza un error 404.
    Verifica que se maneja correctamente el error 404.
    """
    response = client.get('/pagina-inexistente')
    assert response.status_code == 404
    assert b'La pagina no fue encontrada' in response.data

def test_internal_server_error(client):
    """
    Test para simular un error 500.
    Para este test, puedes provocar un error 500 manualmente modificando el código, 
    pero aquí se asume que la ruta no existe como ejemplo.
    """
    response = client.get('/trigger-error')  # Ruta inexistente o error intencional
    assert response.status_code == 500
    assert b'Error interno del servidor' in response.data

