"""
This module generates an address for delivery service with random street, build and flat numbers
"""
import random
import json
import re


streets_file = 'py110_exam_base.json'  # source file with country, city and streets


def test_mode(*args):
    """
    This function to use test mode
    :param args:
    :return:
    """

    def verify_street_format(generate_address):
        """
        This is a wrapper for a function
        :param generate_address:
        :return: result of wrapper
        """
        def wrapper():
            """
            This function check a validity of street spelling
            :return: generated address or an assert if street spelling is wrong
            """
            if len(args) == 0:
                pattern1 = '.+\n'  # check "enter" at the end of line
                pattern2 = '.+,.+'  # check there is no "," symbol
                result = generate_address().send(None)
                if re.fullmatch(pattern1 and pattern2, result[2]) and type(result[2]) is str:
                    print('Street format is not valid!')
                    raise AssertionError('"{}" street format is not valid!'.format(result[2]))
                else:
                    return result
            else:
                result = generate_address().send(None)
                param = str(args[0])
                if re.findall(param, result[0]) or re.findall(param, result[1]) or re.findall(param, result[2]):
                    result = 'Generated address "{}" matches a template "{}"'.format(result, param)
                    return result
                else:
                    return result

        return wrapper

    return verify_street_format


def get_random_address():
    """
    This function read a json file and extract country, city, and street
    :return: country, city, and street
    """
    with open(streets_file, 'r', encoding='utf-8') as f:
        file = json.load(f)
        country = random.choice(file.get("country"))
        city = random.choice(file.get("city"))
        street = random.choice(file.get("street"))
        return country, city, street


@test_mode("переулок")  # This is a test mode
# @test_mode()  # This is a default mode to generate address
def generate_address():
    """
    This function generates a random house and flat and get country, city, street
    :return: country, city, street, house, flat
    """
    while True:
        house = random.randint(1, 50)
        flat = random.randint(1, 230)
        country, city, street = get_random_address()
        yield country, city, street, house, flat


if __name__ == "__main__":
    for i in range(4):
        print(generate_address())
