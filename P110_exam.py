"""
Description of this module
"""
import random
import json
import re


streets_file = 'py110_exam_base.json'


def check_street_json(input_city_country):
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
            file = json.load(f)
            for key in file:
                # print(key['street'])
                if re.findall(pattern, key['street']) is None:
                    print('Format of street is not valid: {}'.format(key['street']))
                else:
                    pass
        return input_city_country()
    return wrapper


@check_street_json
def input_city_country():
    """
    This function request country and city

    Returns City and Country
    -------

    """
    print('Please input city:')
    city = input()
    print('Please input country:')
    country = input()
    return city, country


def get_random_street():
    with open(streets_file, 'r', encoding='utf-8') as f:
        file = json.load(f)
        street = random.choice(file)['street']
        return street


def generate_address():
    house = random.randint(1, 10)
    flat = random.randint(10, 20)
    city, country = input_city_country()
    street = get_random_street()
    print("Random address is:\ncountry: {}\ncity: {}\nstreet :{}\nhouse: {}\nflat {}".
          format(country, city, street, house, flat))


generate_address()
