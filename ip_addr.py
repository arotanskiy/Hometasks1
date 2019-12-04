import random
import re


def get_template(func):
    def wrapper():
        try:
            ip_base = ip_template
        except NameError:
            ip_base = [[], [], [], []]
        print(ip_template)
        result = func(ip_base)
        return result
    return wrapper

def ip_range_define(octet):
    for i in octet:
        if i and '-' in i:
            tmp = i.split('-', 1)
            ip_min = int(tmp[0])
            ip_max = int(tmp[1])
            if ip_max > 255:
                print('IP template is out of range 0 - 255')
                exit(1)
        elif i:
            ip_min = int(i)
            ip_max = int(i)
            if ip_max > 255:
                print('IP template is out of range 0 - 255')
                exit(1)
    return ip_min, ip_max

@get_template
def gen_ip(ip_base):
    while True:
        octet = []
        for octets in ip_base:
            if not octets:
                octet.append(str(random.randint(0, 255)))
            else:
                ip_min, ip_max = ip_range_define(octets)
                octet.append(str(random.randint(ip_min, ip_max)))
        ip = yield ".".join(octet)
        if ip is not None:
            ip_base = ip
            # print(ip_base)


if __name__ == "__main__":
    ip_template = [['10'], ['0-10'], ['10-250'], []]
    my_gen = gen_ip()
    for _ in range(10):
        print(my_gen.send(None))
        # my_gen.send(None)
