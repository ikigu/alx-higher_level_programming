#!/usr/bin/python3

"""Function that writes an Object to text file,
using JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file as JSON"""
    `
    with open(filename, 'w', encoding='utf-8') as f:
        json_text = json.dumps(my_obj)

        f.write(json_text)
