"""
Este módulo contiene pruebas unitarias para la aplicación Flask en app.py.
"""

import pytest
from app import app

@pytest.fixture(name="test_client")
def test_client():
    """Crea un cliente de prueba para la aplicación Flask."""
    with app.test_client() as client:
        yield client

def test_home(app_test_client):
    """Prueba que la ruta principal devuelve el mensaje esperado."""
    response = app_test_client.get("/")
    assert response.status_code == 200  # Verifica que el código de estado sea 200
    assert response.data == b"Hello, CI/CD with Docker!"  # Verifica el contenido
