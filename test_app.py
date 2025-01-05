"""
Este módulo contiene pruebas para la aplicación Flask utilizando pytest.
Las pruebas verifican las rutas y el manejo de errores.
"""
import pytest
from app import app

def test_home():
    """
    Test para la ruta principal ("/").
    Verifica que se recibe un mensaje de saludo correcto.
    """
    response = app.app.test_client.get('/')
    assert b'Hello, CI/CD with Docker!' in response.data

def test_about():
    """
    Test para la ruta "/about".
    Verifica que se recibe la información sobre la aplicación.
    """
    response = app.test_client.get('/about')
    assert b'Esta es una aplicacion Flask para demostrar CI/CD con Docker.' in response.data

def test_greet():
    """
    Test para la ruta "/greet/<name>".
    Verifica que se reciba un saludo personalizado cuando se pasa un nombre en la URL.
    """
    name = 'John'
    response = app.test_client.get(f'/greet/{name}')
    assert f'Hello, {name}!'.encode() in response.data

def test_add_valid():
    """
    Test para la ruta "/add" con datos válidos.
    Verifica que la operación de adición devuelva el resultado correcto.
    """
    response = app.test_client.post('/add', json={'a': 10, 'b': 20})
    data = response.get_json()
    assert data['result'] == 30

def test_add_missing_data():
    """
    Test para la ruta "/add" con datos faltantes.
    Verifica que se maneje correctamente el error cuando faltan parámetros.
    """
    response = app.test_client.post('/add', json={'a': 10})
    data = response.get_json()
    assert 'error' in data

def test_add_invalid_data():
    """
    Test para la ruta "/add" con datos inválidos.
    Verifica que se maneje correctamente el error cuando los datos no son válidos.
    """
    response = app.test_client.post('/add', json={'a': 'ten', 'b': 'twenty'})
    data = response.get_json()
    assert 'error' in data

def test_404_error():
    """
    Test para la ruta desconocida que lanza un error 404.
    Verifica que se maneje correctamente el error 404.
    """
    response = app.test_client.get('/nonexistent')
    assert response.status_code == 404
