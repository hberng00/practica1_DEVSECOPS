"""
Este módulo define una aplicación Flask básica para demostrar CI/CD con Docker.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    """Devuelve un mensaje de saludo para la ruta principal."""
    return "Hello, CI/CD with Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
