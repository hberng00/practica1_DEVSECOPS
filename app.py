"""
Este módulo define una aplicación Flask que proporciona una API simple para demostrar 
CI/CD con Docker. Contiene rutas para saludar, agregar números y manejar errores.
"""

from flask import Flask, jsonify

# Crear la aplicación Flask
app = Flask(__name__)

@app.route("/")
def home():
    """
    Ruta principal que devuelve un mensaje de saludo.
    Esta ruta se usa como la página de inicio de la aplicación.
    """
    return "Hello, CI/CD with Docker!"

@app.route("/about")
def about():
    """
    Ruta que devuelve información acerca de la aplicación.
    Proporciona una breve descripción de lo que hace la aplicación.
    """
    return "Esta es una aplicacion Flask para demostrar CI/CD con Docker."

@app.route("/greet/<name>")
def greet(name):
    """
    Ruta que recibe un nombre y devuelve un saludo personalizado.
    Utiliza el parámetro 'name' de la URL para generar el saludo.
    """
    return f"Hello, {name}! Bienvenido a nuestra aplicacion."

@app.errorhandler(404)
def page_not_found(e):
    """
    Maneja el error 404 cuando la página solicitada no existe.
    Devuelve un mensaje de error en formato JSON.
    """
    e=404
    return jsonify({"error": "La pagina no fue encontrada"}), e

@app.errorhandler(500)
def internal_server_error(e):
    """
    Maneja el error 500 cuando ocurre un error interno en el servidor.
    Devuelve un mensaje de error en formato JSON.
    """
    e=500
    return jsonify({"error": "Error interno del servidor"}), e

# Ejecutar la aplicación Flask en el puerto 5000 cuando se ejecuta el script
if __name__ == "__main__":
    app.run( host="0.0.0.0", port=5000)
