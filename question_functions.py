# En este archivo se declaran las funciones que son utilizadas para responder a las preguntas planteadas
from functions import filter_list
from pokemon_api import get_pokemon_list
import logging

def get_pokemons_qty_by_filter(predicate):
    logging.info(f"get_pokemons_qty_by_filter")
    filtered_pokemons_qty=0
    try:

        pokemons=get_pokemon_list(limit=1126,offset=0)
        if pokemons is not None and len(pokemons)>0:
            filtered_pokemons=filter_list(predicate,pokemons)
            filtered_pokemons_qty=len(filtered_pokemons)
        
    except Exception as error:
        logging.exception(f"Exception - get_pokemons_qty_by_filter {error}")
    finally:
        logging.info(f"get_pokemons_qty_by_filter - return {filtered_pokemons_qty}")
        return filtered_pokemons_qty