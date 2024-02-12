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

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        new_list = []

        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

            f.write(Base.to_json_string(new_list))
