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
* Kong API Gateway

## Uso e instalación de microservicios

1. Instalar Docker
Primero, debe descargar [Docker Desktop](https://www.docker.com/products/docker-desktop) en su ordenador Windows o Mac. Si tiene instalado Linux, le recomendamos que consulte en la página de Docker [Install Docker on Linux](https://runnable.com/docker/install-docker-on-linux)

2. Luego, debe ingresar al Símbolo del sistema (en Windows) o a la Terminal (en Linux o Mac) y ejecutar el siguiente comando, para verificar que Docker se haya instalado correctamente:
```sh
$ docker version
```

3. Se debe realizar `pull` de los siguientes contenedores, necesarios para poder ejecutar los microservicios.

    - Postgres 9.5
    ```sh
    $ docker pull postgres:9.5
    ```
    - Kong 0.10.0
    ```sh
    $ docker pull kong:0.10.1
    ```

3. A continuación se muestra la lista de cada uno de los microservicios; los cuales debe realizar pull en su ordenador para hacer uso de cada uno de ellos.

Nombre      | Versión | Comando docker
------------|---------|------------
sumar       | 1.0     | docker pull cesargomez05/sumar
restar      | 1.0     | docker pull cesargomez05/restar
multiplicar | 1.0     | docker pull cesargomez05/multiplicar
dividir     | 1.0     | docker pull cesargomez05/dividir

4. Una vez hecho el `pull` de cada uno de los contenedores que deseamos usar, debemos eejcutar el siguiente comando para que los microservicios se ejecuten dentro de una misma red en Docker.

```sh
docker network create --subnet=172.18.0.0/16 microservicios
```

5. Luego, se debe ejecutar cada una de los contenedores usando los respectivos comandos.

    - Postgres 9.5
    ```sh
    $ docker run -d --net microservicios --ip 172.18.0.6 --name kong-database -p 5432:5432 -e POSTGRES_USER=kong -e POSTGRES_DB=kong -e POSTGRES_HOST_AUTH_METHOD=trust postgres:9.5
    ```

    - Kong
    ```sh
    $ docker run -d --net microservicios --ip 172.18.0.7 --name kong --link kong-database:kong-database -e KONG_DATABASE=postgres -e KONG_PG_HOST=kong-database -p 8000:8000 -p 8443:8443 -p 8001:8001 -p 7946:7946 -p 7946:7946/udp kong:0.10.1
    ```

    - Contenedores de los microservicios
    ```sh
    $ docker run -it --net microservicios --ip 172.18.0.2 -p 4001:4000 -d --name sumar cesargomez05/sumar:1.0
    $ docker run -it --net microservicios --ip 172.18.0.3 -p 4002:4000 -d --name restar cesargomez05/restar:1.0
    $ docker run -it --net microservicios --ip 172.18.0.4 -p 4003:4000 -d --name multiplicar cesargomez05/multiplicar:1.0
    $ docker run -it --net microservicios --ip 172.18.0.5 -p 4004:4000 -d --name dividir cesargomez05/dividir:1.0
    ```

6. En nuestro Símbolo del sistema (en Windows) o Terminal (en Linux o Mac) ejecutamos el siguiente comando; el cual permite listar los contenedores que se encuentren en ejecución dentro de Docker.

```sh
docker ps
```

7. En nuestro navegador web de preferencia (Chrome, Firefox, etc.) ingresamos a la dirección [http://127.0.0.1:8000/](http://127.0.0.1:8000/), y nos debe salir un mensaje en formato JSON como el que se observa a continuación.
```JSON
{"message":"no API found with those values"}
```

8. Ingresamos a nuestro cliente HTTP de preferencia, por ejemplo [Postman](https://www.postman.com/), [Insomnia](https://insomnia.rest/)), o cualquier otro, y ejecutamos el llamado a cada uno de los microservicios.

- Sumar
