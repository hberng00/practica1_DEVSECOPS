from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    """Devuelve un mensaje de saludo para la ruta principal."""
    return "Hello, CI/CD with Docker!"

@app.route("/about")
def about():
    """Devuelve informacion sobre la aplicacion."""
    return "Esta es una aplicacion Flask para demostrar CI/CD con Docker."

@app.route("/greet/<name>")
def greet(name):
    """Devuelve un saludo personalizado."""
    return f"Hello, {name}! Bienvenido a nuestra aplicacion."

@app.route("/add", methods=["POST"])
def add():
    """
    Suma dos numeros enviados en la solicitud POST.
    Espera un JSON en el formato {"a": valor1, "b": valor2}.
    """
    data = request.get_json()
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Debes proporcionar los numeros 'a' y 'b'"}), 400
    
    a = data['a']
    b = data['b']
    
    # Validate that a and b are numbers
    try:
        result = float(a) + float(b)
    except ValueError:
        return jsonify({"error": "Los valores 'a' y 'b' deben ser numeros"}), 400
    
    return jsonify({"result": result})

@app.errorhandler(404)
def page_not_found():
    """Maneja errores 404 y devuelve un mensaje personalizado."""
    return jsonify({"error": "La pagina no fue encontrada"}), 404

@app.errorhandler(500)
def internal_server_error():
    """Maneja errores 500 y devuelve un mensaje personalizado."""
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
