# En este archivo se declaran funciones genéricas
# Las cuales en caso de ser necesario podrían ser reutilizadas más de una vez.
import logging

from pokemon_api import get_element_data_by_name

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