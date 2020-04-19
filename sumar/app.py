from flask import Flask, jsonify, request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify(message="La opción a ejecutar no es válida")

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
@validate_params
def sumar(num1, num2):
    return jsonify(result=num1 + num2)

if __name__ == '__main__':
    # Se define el puerto en el cual se ejecutará la solución
    port = 4000
    host = '0.0.0.0'
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host=host, port=port)