import pytest
from flask import Flask
from app import app  # Asumiendo que tu código está en un archivo llamado app.py

# Usamos el fixture de pytest para el cliente de pruebas de Flask
@pytest.fixture
def client():
    # Creamos un cliente de prueba para nuestra aplicación Flask
    with app.test_client() as client:
        yield client

# Test para la ruta principal "/"
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode() == "Hello, CI/CD with Docker!"

# Test para la ruta "/about"
def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert response.data.decode() == "Esta es una aplicacion Flask para demostrar CI/CD con Docker."

# Test para la ruta "/greet/<name>"
def test_greet(client):
    name = "Juan"
    response = client.get(f"/greet/{name}")
    assert response.status_code == 200
    assert response.data.decode() == f"Hello, {name}! Bienvenido a nuestra aplicacion."

# Test para el manejo de error 404
def test_page_not_found(client):
    response = client.get("/pagina_inexistente")
    assert response.status_code == 404
    assert response.json == {"error": "La pagina no fue encontrada"}

# Test para el manejo de error 500
def test_internal_server_error(client):
    # Simulamos un error 500 provocando un fallo en el servidor
    @app.route("/error")
    def error_route():
        raise Exception("Error forzado")
    
    response = client.get("/error")
    assert response.status_code == 500
    assert response.json == {"error": "Error interno del servidor"}
