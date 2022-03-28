# En este archivo se declaran funciones genéricas
# Las cuales en caso de ser necesario podrían ser reutilizadas más de una vez.
import logging

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



