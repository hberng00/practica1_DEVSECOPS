from flask import Flask, jsonify, request

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

@app.route("/add", methods=["POST"])
def add():
    """
    Ruta que suma dos números enviados en una solicitud POST.
    Se espera que los datos se envíen en formato JSON con las claves 'a' y 'b'.
    Ejemplo de entrada JSON: {"a": 10, "b": 20}
    
    Devuelve un resultado en formato JSON con la clave 'result' que contiene la suma de los dos números.
    """
    data = request.get_json()
    
    # Verificar si los datos son válidos y si contienen 'a' y 'b'
    if not data or 'a' not in data or 'b' not in data:
        return jsonify({"error": "Debes proporcionar los numeros 'a' y 'b'"}), 400
    
    a = data['a']
    b = data['b']
    
    # Validar que 'a' y 'b' sean números
    try:
        result = float(a) + float(b)
    except ValueError:
        return jsonify({"error": "Los valores 'a' y 'b' deben ser numeros"}), 400
    
    return jsonify({"result": result})

@app.errorhandler(404)
def page_not_found():
    """
    Maneja el error 404 cuando la página solicitada no existe.
    Devuelve un mensaje de error en formato JSON.
    """
    return jsonify({"error": "La pagina no fue encontrada"}), 404

@app.errorhandler(500)
def internal_server_error():
    """
    Maneja el error 500 cuando ocurre un error interno en el servidor.
    Devuelve un mensaje de error en formato JSON.
    """
    return jsonify({"error": "Error interno del servidor"}), 500

# Ejecutar la aplicación Flask en el puerto 5000 cuando se ejecuta el script
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
