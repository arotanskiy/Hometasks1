"""
Description of this module
"""
import random
import json
import re


streets_file = 'py110_exam_base.json'


def verify_street_json(get_random_address):
    """
    This func check a validity of streets spelling
    Parameters
    ----------
    input_city_country

    Returns wrapped function
    -------

    """
    def wrapper():
        # полный генератор
        # проаерка параметра переданного через фабрику
        pattern = '\d+'
        with open(streets_file, 'r', encoding='utf-8') as f:
            database = json.load(f)
            streets = database.get("street")
            for key in streets:
                if re.findall(pattern, key) is None:
                    print('Format of street is not valid: {}'.format(key))
                else:
                    pass
        return get_random_address()
    return wrapper


@verify_street_json
def get_random_address():
    with open(streets_file, 'r', encoding='utf-8') as f:
        file = json.load(f)
        country = random.choice(file.get("country"))
        city = random.choice(file.get("city"))
        street = random.choice(file.get("street"))
        return country, city, street


def generate_address():
    house = random.randint(1, 30)
    flat = random.randint(1, 20)
    country, city, street = get_random_address()
    print("Random address is:\ncountry: {}\ncity: {}\nstreet :{}\nhouse: {}\nflat {}".
          format(country, city, street, house, flat))


generate_address()
