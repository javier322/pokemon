# En este archivo se realiza el llamado a las funciones necesarias para responder las preguntas planteadas
from email.policy import default
import logging
from question_functions import get_pokemons_qty_by_filter
from decouple import config
ENV_MODE=config("ENV_MODE",default="")

def answer_question_one():
    logging.info("answer_question_one")
    first_condition= lambda pokemon: pokemon.get('name',None).find('at')!=-1 
    second_condition= lambda pokemon: pokemon.get('name',None).count('a')==2
    predicate= lambda pokemon: first_condition(pokemon) and second_condition(pokemon)

    pokemon_qty=get_pokemons_qty_by_filter(predicate)

    print(f"La cantidad de pokemones que poseen \"at\" en su nombre e incluyen 2 letras \"a\" es de {pokemon_qty}\n")


if __name__ == "__main__":
    print(ENV_MODE)
    if ENV_MODE=="prod":
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename="app.log",filemode="w",
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    else:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)

    
    answer_question_one()