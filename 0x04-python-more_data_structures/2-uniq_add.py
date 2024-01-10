#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_from_list = set(my_list)
    result = 0

    for item in set_from_list:
        result += item

    return result
