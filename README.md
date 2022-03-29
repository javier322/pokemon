# Desafío Pokémon

A continuación se proveen las instrucciones necesarias para ejecutar el programa que permite responder las preguntas planteadas en el contexto del desafío propuesto.

## Dependencias y versiones

Este programa se implementó a partir de la versión 3.8 de python. Así mismo, se utilizaron las siguientes bibliotecas externas:

 - requests versión 2.22.0
 - python-decouple versión 3.6
 - requests-cache versión 0.9.3

Dichas bibliotecas se encuentran listadas en el archivo requirements.txt y pueden ser instaladas con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecución

Existen dos formas disponibles para ejecutar el programa y obtener las respuestas a las preguntas planteadas. Esto puede ser a través de la versión local que se tenga instalada de python o con Docker. En ambos casos primero es necesario clonar todo el contenido del repositorio y definir las variables de configuración a través del archivo .env

### Local
La lógica principal del código se encuentra declarada en el archivo main.py. Por lo tanto, para ejecutar el programa se debe ingresar el siguiente comando:

```bash
python3 main.py
``` 

Un aspecto importante en este modo de ejecución corresponde al hecho de que las peticiones realizadas a la API REST de pokémon se guardan en un caché por 1 minuto a partir de la biblioteca requests_cache, de tal forma que las siguientes ejecuciones son más rápidas durante este intervalo.
## Docker

Para ejecutar el programa a través de Docker, se provee un archivo Dockerfile así como 2 script buildDocker.sh y runDocker.sh, los cuales se deben ejecutar en orden:

 - Este script  solo se debe ejecutar la primera vez para crear la imagen Docker, la carpeta con los archivos de salida y el volumen asociado a esta:

```bash
sudo ./buildDocker.sh
```
 - Posteriormente, cada vez que se desee correr el programa se debe ejecutar el otro script.

```bash
sudo ./runDocker.sh
```


En este modo de ejecución las peticiones no se guardan en cache, debido a que el contenedor Docker se crea de forma momentanea para ejecutar el programa y posteriormente se elimina junto con los archivos asociados al caché.
## Salida

Como resultado de ejecutar el programa se listan las respuestas a las preguntas planteadas y también estas se escriben en un archivo de texto que se genera en la carpeta de salida (output). Adicionalmente, dependiendo si este programa se ejecuta en modo producción (prod) o desarrollo (dev) se genera un archivo que contiene los logs asociados a la ejecución o estos se imprimen en el terminal. Dichas variables se definen en el archivo .env tal como se explica en la siguiente sección.

## Configuración

Existen diferentes variables de configuración que se deben definir en un archivo .env para poder ejecutar el programa correctamente. A modo de referencia se puede encontrar un archivo .env.example que puedser ser utilizado si se le cambia el nombre a .env. Las variables que se deben definir en dicho archivo corresponden a las siguientes:

 - POKEMON_API_URL: Corresponde a la url base de la API REST para poder consumir los servicios de pokémon. Por defecto asume el valor de https://pokeapi.co/api/v2.
- ENV_MODE: Corresponde al modo de ambiente de ejecución, los cuales pueden ser prod o dev. En el primer caso se genera un archivo .log con los logs registrados para la ejecución, de lo contrario, estos se listan a través del terminal. Por defecto asume el valor de dev.
- LOG_FILE: Corresponde al nombre del archivo en el cual se generan los logs en caso de ejecutar el programa en modo prod. Por defecto asume el nombre de app.log.
 - OUTPUT_FILE: Corresponde al nombre del archivo en el cual se escriben las respuestas a las preguntas planteadas. Por defecto asume el nombre de answers.txt.
