from flask import Flask, jsonify, request, make_response
from functools import wraps
import json

app = Flask(__name__)

with open("database.json", "r") as f:
    users = json.load(f)

# Función decorador que se ejecuta para validar el acceso a los microservicios
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Se obtiene el valor encriptado de usuario y contraseña
        auth = request.headers.get("Authorization")
        method = "Basic "

        if request.authorization and request.authorization.username and request.authorization.password:
            if request.authorization.username in users:
                if method + users[request.authorization.username]['token'] == auth:
                    return f(*args, **kwargs)
            return jsonify({"message": "ERROR: Usuario no autorizado"}), 401

        return make_response('No fue posible verificar el inicio de sesión', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
    return decorated

# Función decoradora para validar los dos parámetros de la función
def validate_params(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        args = request.args

        # Se valida si en el objeto de argumentos se definió los valores
        if "num1" not in args or "num2" not in args:
            return jsonify(message="Por favor define los parámetros 'num1' y 'num2'")

        num1 = request.args.get("num1", type=int)
        num2 = request.args.get("num2", type=int)

        # Se valida si alguno de los valores no son números
        if num1 is None or num2 is None:
            return jsonify(message="Por favor define un valor entero en los parámetros 'num1' y 'num2'")

        return f(num1, num2)
    return decorated

# Ruta de inicio para validar funcionamiento de la aplicación en Flask
@app.route('/', methods = ['POST'])
@auth_required
def home():
    return jsonify(state="OK")

# Ruta para el servicio de sumar valores
@app.route('/sumar', methods = ['POST'])
@auth_required
@validate_params
def sumar(num1, num2):
    return jsonify(result=num1 + num2)

# Ruta para el servicio de restar valores
@app.route('/restar', methods = ['POST'])
@auth_required
@validate_params
def restar(num1, num2):
    return jsonify(result=num1 - num2)

# Ruta para el servicio de multiplicar valores
@app.route('/multiplicar', methods = ['POST'])
@auth_required
@validate_params
def multiplicar(num1, num2):
    return jsonify(result=num1 * num2)

# Ruta para el servicio de dividir valores
@app.route('/dividir', methods = ['POST'])
@auth_required
@validate_params
def dividir(num1, num2):
    if num2 == 0:
        return jsonify(message="No se puede dividir entre cero")
    return jsonify(result=num1 / num2)

if __name__ == '__main__':
    # Se define el puerto en el cual se ejecutará la solución
    port = 4000
    # Se habilita el modo debug para visualizar errores
    app.debug = True
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host='0.0.0.0', port=port)