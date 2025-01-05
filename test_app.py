""" 
Módulo de pruebas para la aplicación Flask. 
Contiene tests para verificar el funcionamiento de las rutas y manejo de errores.
"""

import pytest
from app import app  # Asumiendo que tu código está en un archivo llamado app.py

@pytest.fixture
def cliente_prueba():
    """
    Fixture que crea un cliente de prueba para simular las peticiones HTTP a la aplicación Flask.
    """
    with app.test_client() as client:
        yield client

def test_home(cliente_prueba):
    """Test de la ruta principal /"""
    response = cliente_prueba.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello, CI/CD with Docker!"

def test_about(cliente_prueba):
    """Test de la ruta /about"""
    response = cliente_prueba.get("/about")
    assert response.status_code == 200
    assert response.data.decode() == "Esta es una aplicacion Flask para demostrar CI/CD con Docker."

def test_greet(cliente_prueba):
    """Test de la ruta /greet/<name>"""
    name = "Juan"
    response = cliente_prueba.get(f"/greet/{name}")
    assert response.status_code == 200
    assert response.data.decode() == f"Hello, {name}! Bienvenido a nuestra aplicacion."

def test_page_not_found(cliente_prueba):
    """Test para el manejo de error 404"""
    response = cliente_prueba.get("/pagina_inexistente")
    assert response.status_code == 404
    assert response.json == {"error": "La pagina no fue encontrada"}

def test_internal_server_error(cliente_prueba):
    """Test para el manejo de error 500"""
    # Simulamos un error 500 provocando un fallo en el servidor
    @app.route("/error")
    def error_route():
        raise RuntimeError("Error forzado")  # Cambiar a un error más específico
    
    response = cliente_prueba.get("/error")
    assert response.status_code == 500
    assert response.json == {"error": "Error interno del servidor"}
