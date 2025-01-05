""" 
Módulo de pruebas para la aplicación Flask. 
Contiene tests para verificar el funcionamiento de las rutas y manejo de errores.
"""

import pytest
from app import app  # Asumiendo que tu código está en un archivo llamado app.py

@pytest.fixture
def test_client():
    """
    Fixture que crea un cliente de prueba para simular las peticiones HTTP a la aplicación Flask.
    """
    with app.test_client() as client:
        yield client

def test_home(test_client):
    """Test de la ruta principal /"""
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello, CI/CD with Docker!"

def test_about(test_client):
    """Test de la ruta /about"""
    response = test_client.get("/about")
    assert response.status_code == 200
    assert response.data.decode() == "Esta es una aplicacion Flask para demostrar CI/CD con Docker."

def test_greet(test_client):
    """Test de la ruta /greet/<name>"""
    name = "Juan"
    response = test_client.get(f"/greet/{name}")
    assert response.status_code == 200
    assert response.data.decode() == f"Hello, {name}! Bienvenido a nuestra aplicacion."

def test_page_not_found(test_client):
    """Test para el manejo de error 404"""
    response = test_client.get("/pagina_inexistente")
    assert response.status_code == 404
    assert response.json == {"error": "La pagina no fue encontrada"}

def test_internal_server_error(test_client):
    """Test para el manejo de error 500"""
    # Simulamos un error 500 provocando un fallo en el servidor
    @app.route("/error")
    def error_route():
        raise RuntimeError("Error forzado")  # Cambiar a un error más específico
    
    response = test_client.get("/error")
    assert response.status_code == 500
    assert response.json == {"error": "Error interno del servidor"}
