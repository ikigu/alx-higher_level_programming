#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary == None:
        return None

    value: int = 0
    key: str = ""

    for k, v in a_dictionary.items():
        if a_dictionary[k] > value:
            value = v
            key = k

    return key
