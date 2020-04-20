# Ejercicio Microservicios con Flask

## Integrantes
* Laura Alejandra Campos - 20201099028
* Steven Fabián Gómez - 20201099030
* César Augusto Gómez - 20201099031
* Edna Nayibe Palma - 20201099041

## Objetivo de la solución
Establecer una arquitectura orientada a microservicios usando el micro-framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) para ofrecer la implementación de los servicios de suma, resta, multiplicación y división.

## Tecnologías empleadas

* Python 3.7 
* Flask 1.1.2
* Docker
* Kong

## Uso e instalación de microservicios

1. Instalar Docker
Primero, debe descargar [Docker Desktop](https://www.docker.com/products/docker-desktop) en su ordenador Windows o Mac. Si tiene instalado Linux, le recomendamos que consulte en la página de Docker [Install Docker on Linux](https://runnable.com/docker/install-docker-on-linux)

2. Luego, debe ingresar al Símbolo de sistema (en Windows) o a la Terminal (en Linux o Mac) y ejecutar el siguiente comando, para verificar que Docker se haya instalado correctamente:
> docker version

3. Se debe realizar `pull` de los siguientes contenedores

    - Postgres 9.5
    > docker pull postgres:9.5
    - Kong 0.10.0
    > docker pull kong:0.10.1

3. A continuación se muestra la lista de cada uno de los microservicios; los cuales debe realizar pull en su ordenador para hacer uso de cada uno de ellos.

Nombre      | Versión | Comando docker
------------|---------|------------
sumar       | 1.0     | docker pull cesargomez05/dividir
restar      | 1.0     | docker pull cesargomez05/dividir
multiplicar | 1.0     | docker pull cesargomez05/dividir
dividir     | 1.0     | docker pull cesargomez05/dividir

4. Una vez hecho el `pull` de cada uno de los contenedores que deseamos usar, debemos hacer el mismo procedimiento para 
> docker network create --subnet=172.18.0.0/16 microservicios

5. 
