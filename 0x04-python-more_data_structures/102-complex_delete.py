#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for k, _ in list(a_dictionary.items()):
        if a_dictionary[k] == value:
            del a_dictionary[k]

    return a_dictionary
