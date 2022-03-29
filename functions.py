""" 
En este archivo se declaran funciones que son usadas para construir las funciones principales
vinculadas a las preguntas planteadas
"""
from cmath import inf
from pokemon_api import get_element_data_by_name
import logging

# Función que permite filtrar datos de una lista en base a un predicado dado
def filter_list(predicate, data):
    logging.info(f"filter_list - data {len(data)} elements")
    filtered_list=data.copy()
    try:
        filtered_list=list(filter(predicate,data))
    except Exception as error:
        logging.error(f"filter_list Exception {error}",exc_info=True)
    finally:
        logging.info(f"filter_list - return {len(filtered_list)} elements")
        return filtered_list

# Función que permite obtener una lista con todas las especies asociadas a 1 o múltiples egg groups
def get_egg_groups_species(pokemon_egg_groups=[]):
    logging.info(f"get_egg_groups_species - pokemon_egg_groups {len(pokemon_egg_groups)} elements")
    pokemon_species_list=[]
    try:
        for egg_group in pokemon_egg_groups:
            egg_group_name=egg_group.get("name","")
            egg_group_data=get_element_data_by_name("egg-group",egg_group_name)
            egg_group_species= egg_group_data.get("pokemon_species",[])
            pokemon_species_list= pokemon_species_list+ egg_group_species
    except Exception as error:
        logging.exception(f"get_egg_groups_species Exception {error}")
    finally:
        logging.info(f"get_egg_groups_species - return {len(pokemon_species_list)} elements")
        return pokemon_species_list

# Función que permite obtener y filtrar pokemones por generación
def filter_pokemons_by_generation(pokemons=[],max_id=0,min_id=0):
    logging.info(f"filter_pokemons_by_generation -  pokemons {len(pokemons)} elements, max_id {max_id}, min_id {min_id}")
    filtered_pokemon_list=[]
    try:

        for pokemon in pokemons:
            pokemon_dict=pokemon.get("pokemon",dict())
            pokemon_name=pokemon_dict.get("name","")
            pokemon_data=get_element_data_by_name("pokemon",pokemon_name)
            pokemon_id=pokemon_data.get("id",0)

            if pokemon_id>=min_id and pokemon_id<=max_id:
                filtered_pokemon_list.append(pokemon_data)
            elif pokemon_id>max_id:
                break

    except Exception as error:
        logging.exception(f"filter_pokemons_by_generation Exception {error}")
    finally:
        logging.info(f"filter_pokemons_by_generation - return {len(filtered_pokemon_list)} elements")
        return filtered_pokemon_list

# Función que permite obtener pesos máximos y mínimados dada la lista de pesos
def get_max_min_weight(filtered_pokemon_list_weight):
    logging.info(f"get_max_min_weight - filtered_pokemon_list {len(filtered_pokemon_list_weight)} elements")
    max_min_weight=[0,inf]
    try:
        for weight in filtered_pokemon_list_weight:
            if weight > max_min_weight[0]:
                max_min_weight[0]=weight
            if weight < max_min_weight[1]:
                max_min_weight[1]=weight
    except Exception as error:
        logging.exception(f"get_max_min_weight Exception {error}")
    finally:
        logging.info(f"get_max_min_weight - return max weight {max_min_weight[0]}, min weight {max_min_weight[1]}")
        return max_min_weight