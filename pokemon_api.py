
"""
En este archivo se declaran las funciones necesarias para interactuar con la API REST de pokémon
"""


import requests
import logging
from decouple import config

POKEMON_API_URL=config("POKEMON_API_URL",default="https://pokeapi.co/api/v2")


# Función genérica para llevar a cabo peticiones REST de tipo GET.
def get_request(url):
    logging.info(f"get_request- GET HTTP {url}")
    response_json=dict()
    try:
        response=requests.get(url,timeout=2)
        response.raise_for_status()
        if response is not None:
            response_json=response.json()


    except requests.exceptions.HTTPError as http_error:
        logging.exception(f"get_request HTTP Error {http_error}")
    except requests.exceptions.ConnectionError as connection_error:
        logging.exception(f"get_request Connection Error {connection_error}")
    except requests.exceptions.Timeout as timeout_error:
        logging.exception(f"get_request Timeout Error {timeout_error}")
    except requests.exceptions.RequestException as request_error:
        logging.exception(f"get_request Request Error {request_error}")
    except Exception as general_error:
        logging.exception(f"get_request Exception {general_error}")
    finally:
        logging.info(f"get_request - return dict with {len(response_json)} fields")
        return response_json


# Función que permite obtener lista de pokemones a través de la API.
def get_pokemon_list(limit=20,offset=0):
    logging.info(f"get_pokemon_list - limit={limit}, offset={offset}")
    pokemon_list=[]
    try:
        url= f"{POKEMON_API_URL}/pokemon/?limit={limit}&offset={offset}"
        response_json=get_request(url)
        if response_json is not None:
            pokemon_list=response_json.get("results",[])
    except Exception as general_error:
        logging.exception(f"get_pokemon_list Exception {general_error}")
    finally:
        logging.info(f"get_pokemon_list - return {len(pokemon_list)} elements")
        return pokemon_list


# Función que permite obtener los datos de un elemento específico a partir de su nombre (pokemons, species, egg groups, etc)
def get_element_data_by_name(route="/",name=""):
    logging.info(f"get_element_data_by_name - route={route}, name {name}")
    element=dict()
    try:
        url=f"{POKEMON_API_URL}/{route}/{name}"
        response_json=get_request(url)
        if response_json is not None:
            element=response_json
    except Exception as error:
        logging.exception(f"get_element_data_by_name Exception {error}")
    finally:
        logging.info(f"get_element_data_by_name - return {len(element)} fields")
        return element

# Función que permite obtener la lista de pokemones por tipo
def get_pokemon_list_by_type(type):
    logging.info(f"get_pokemon_list_by_type - type {type}")
    pokemon_list=[]
    try:
        url=f"{POKEMON_API_URL}/type/{type}"
        response_json=get_request(url)

        if response_json is not None:
            pokemon_list=response_json.get("pokemon",[])
    except Exception as error:
        logging.exception(f"get_pokemon_list_by_type Exception {error}")
    finally:
        logging.info(f"get_pokemon_list_by_type - return {len(pokemon_list)} elements")
        return pokemon_list