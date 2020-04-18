from flask import Flask, jsonify, request, make_response
from functools import wraps

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify(message="La opción a ejecutar no es válida")

# Ruta de inicio para validar funcionamiento de la aplicación en Flask
@app.route('/', methods = ['POST'])
def sumar():
    args = request.args

    # Se valida si en el objeto de argumentos se definió los valores
    if "num1" not in args or "num2" not in args:
        return jsonify(message="Por favor define los parámetros 'num1' y 'num2'")

    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)

    # Se valida si alguno de los valores no son números
    if num1 is None or num2 is None:
        return jsonify(message="Por favor define un valor entero en los parámetros 'num1' y 'num2'")

    return jsonify(result=num1 + num2)

if __name__ == '__main__':
    # Se define el puerto en el cual se ejecutará la solución
    port = 4001
    # Se habilita el modo debug para visualizar errores
    app.debug = True
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host='0.0.0.0', port=port)