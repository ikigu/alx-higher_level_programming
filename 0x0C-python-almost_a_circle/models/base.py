#!/usr/bin/python3

"""My Base class"""


import json


class Base():
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def __del__(self):
        if Base.__nb_objects >= 1:
            Base.__nb_objects -= 1

        del self

    @staticmethod
    def to_json_string(list_dictionaries):
        """Turn to json"""
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
