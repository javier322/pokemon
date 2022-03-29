"""En este archivo se realiza el llamado a las funciones necesarias para responder las preguntas planteadas"""



from question_functions import get_pokemon_egg_group_qty, get_pokemon_max_min_weight, get_pokemons_qty_by_filter
from decouple import config
import logging
import requests_cache
import os


ENV_MODE=config("ENV_MODE",default="dev")
OUTPUT_FILE=config("OUTPUT_FILE",default="answers.txt")
LOG_FILE=config("LOG_FILE",default="app.log")

OUTPUT_FILE="output"

# Respuesta pregunta 1
def answer_question_one():
    logging.info("answer_question_one")
    answer=""
    try:

        first_condition= lambda pokemon: pokemon.get('name',None).find('at')!=-1 
        second_condition= lambda pokemon: pokemon.get('name',None).count('a')==2
        predicate= lambda pokemon: first_condition(pokemon) and second_condition(pokemon)

        pokemon_qty=get_pokemons_qty_by_filter(predicate)

        answer= f"1) La cantidad de pokemones que poseen \"at\" en su nombre e incluyen 2 letras \"a\" es de {pokemon_qty}\n"
    except Exception as error:
        logging.exception(f"answer_question_one Exception {error}")
    finally:
        return answer

# Respuesta pregunta 2
def answer_question_two():
    logging.info("answer_question_two")
    answer=""
    try:

        pokemon_egg_group_qty=get_pokemon_egg_group_qty("raichu")

        answer =f"2) La cantidad de especies con las cuales puede procrear raichu corresponde a {pokemon_egg_group_qty}\n"
    except Exception as error:
        logging.exception(f"answer_question_two Exception {error}")
    finally:
        return answer

# Respuesta pregunta 3
def answer_question_three():
    logging.info("answer_question_three")
    answer=""
    try:
        pokemon_max_min_weight=get_pokemon_max_min_weight("fighting",151,1)
        answer=f"3) El peso máximo y minimo de los pokemones de tipo fighting de la primera generación es de {pokemon_max_min_weight} respectivamente\n"
    except Exception as error:
        logging.exception(f"answer_question_three Exception {error}")
    finally:
        return answer


def write_answers_to_file(answer_one,answer_two,answer_three):

    logging.info("write_answers_to_file")
    try:

        with open(f"{OUTPUT_FILE}/answers.txt","w") as file:
            file.writelines(answer_one)
            file.writelines(answer_two)
            file.writelines(answer_three)
    except Exception as error:
        logging.exception(f"write_answers_to_file Exception {error}")

def write_answers_to_console(answer_one,answer_two,answer_three):

    logging.info(write_answers_to_console)
    try:
        print("\n")
        print(answer_one)
        print(answer_two)
        print(answer_three)
    except Exception as error:
        logging.exception(f"write_answers_to_console Exception {error}")


#Flujo principal
if __name__ == "__main__":
    if not os.path.exists(OUTPUT_FILE):
        os.makedirs(OUTPUT_FILE,mode=0o777)

    if ENV_MODE=="prod":
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename=f"{OUTPUT_FILE}/{LOG_FILE}",filemode="w",
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    else:
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)

    # Cache con duración de 1 minuto
    requests_cache.install_cache('pokemon_api_cache', backend='filesystem', expire_after=60)
    
    answer_one=answer_question_one()
    answer_two=answer_question_two()
    answer_three=answer_question_three()

    write_answers_to_file(answer_one,answer_two,answer_three)
    write_answers_to_console(answer_one,answer_two,answer_three)
  