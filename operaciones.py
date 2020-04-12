from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)

with open("database.json", "r") as f:
    users = json.load(f)

# Ruta de inicio para validar funcionamiento de la aplicación en Flask
@app.route('/', methods = ['GET', 'POST'])
def home():
    auth = request.headers.get("Authorization")
    method = "Basic "

    if request.authorization and request.authorization.username and request.authorization.password:
        if request.authorization.username not in users:
            return jsonify({"message": "ERROR: Unauthorized"}), 401
        elif method + users[request.authorization.username]['token'] == auth:
            return jsonify(operation="OK")
        else:
            return jsonify({"message": "ERROR: Unauthorized"}), 401

    return make_response('No podemos', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

# Ruta para el servicio de sumar valores
@app.route('/sumar', methods = ['GET', 'POST'])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")

    resultado = num1 + num2
    return jsonify(operation="Sumar",valor=resultado)

# Ruta para el servicio de restar valores
@app.route('/restar', methods = ['GET', 'POST'])
def restar():
    return jsonify(operation="Restar")

# Ruta para el servicio de multiplicar valores
@app.route('/multiplicar', methods = ['GET', 'POST'])
def multiplicar():
    return jsonify(operation="Multiplicar")

# Ruta para el servicio de dividir valores
@app.route('/dividir', methods = ['GET', 'POST'])
def dividir():
    return jsonify(operation="Dividir")

if __name__ == '__main__':
    # Se define el puerto en el cual se ejecutará la solución
    port = 4000
    # Se habilita el modo debug para visualizar errores
    app.debug = True
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host='0.0.0.0', port=port)