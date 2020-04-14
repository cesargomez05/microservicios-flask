# Ejercicio Microservicios con Flask

## Integrantes
* Laura Alejandra Campos - 20201099028
* Steven Fabián Gómez - 20201099030
* César Augusto Gómez - 20201099031
* Edna Nayibe Palma - 20201099041

## Objetivo de la solución
Establecer una arquitectura orientada a microservicios usando el micro-framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) para ofrecer la implementación de los servicios de suma, resta, multiplicación y división.

## Tecnologías empleadas
* Python 3.8.2
* Flask 1.1.2
* Docker

## Pasos para ejecución
1. Ejecutar cada uno de los scripts en Python
> python servicios/sumar.py
> python servicios/restar.py
> python servicios/multiplicar.py
> python servicios/dividir.py

2. Utilizar un cliente web (por ejemplo, Postman) para ejecutar cada uno de los servicios

* Servicio de suma
> http://127.0.0.1:4001/sumar?num1=176&num2=65
* Servicio de resta
> http://127.0.0.1:4002/restar?num1=176&num2=65
* Servicio de multiplicación
> http://127.0.0.1:4003/multiplicar?num1=176&num2=65
* Servicio de división
> http://127.0.0.1:4004/dividir?num1=176&num2=65
