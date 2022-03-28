# En este archivo se declaran las funciones que son utilizadas para responder a las preguntas planteadas
from functions import filter_list, get_egg_groups_species
from pokemon_api import get_element_data_by_name, get_pokemon_list
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
        logging.exception(f"get_pokemons_qty_by_filter Exception {error}")
    finally:
        logging.info(f"get_pokemons_qty_by_filter - return {filtered_pokemons_qty}")
        return filtered_pokemons_qty

def get_pokemon_egg_group_qty(name):
    logging.info(f"get_pokemon_egg_group_qty - name={name}")
    pokemon_egg_group_qty=0
    try:

        pokemon_data=get_element_data_by_name("pokemon",name)
        pokemon_specie=pokemon_data.get("species",dict())
        pokemon_specie_name=pokemon_specie.get("name","")

        pokemon_specie_data=get_element_data_by_name("pokemon-species",pokemon_specie_name)
        pokemon_egg_groups=pokemon_specie_data.get("egg_groups",[])
        pokemon_species_list=get_egg_groups_species(pokemon_egg_groups)
        
        pokemon_species_names=map(lambda specie: specie.get("name",""), pokemon_species_list)
        pokemon_species_set=set(pokemon_species_names)
        pokemon_egg_group_qty=len(pokemon_species_set)
    except Exception as error:
        logging.exception(f"get_pokemon_egg_group_qty Exception {error}")
    finally:
        logging.info(f"get_pokemon_egg_group_qty - return {pokemon_egg_group_qty} ")
        return pokemon_egg_group_qty

        




