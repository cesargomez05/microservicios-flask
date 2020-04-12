from flask import Flask, jsonify, request

app = Flask(__name__)

# Ruta de inicio para validar funcionamiento de la aplicación en Flask
@app.route('/', methods = ['GET'])
def home():
	return jsonify(status="OK")

# Ruta para el servicio de sumar valores
@app.route('/sumar', methods = ['GET', 'POST'])
def sumar():
    return jsonify(operation="Sumar")

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