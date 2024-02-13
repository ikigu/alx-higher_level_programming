#!/usr/bin/python3

"""My Base class"""


import json
import os


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
        """Saves Base object to a json file with class name"""
        file_name = cls.__name__ + ".json"
        new_list = []

        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                return f.write("[]")
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())

            f.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Static method to convert string to object"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls) -> list:
        """Reads from json file and loads a list into a Python object"""
        filepath = cls.__name__ + ".json"

        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return_list = []
                content = f.read()
                content_object = cls.from_json_string(content)

                for item in content_object:
                    return_list.append(cls.create(**item))
                return return_list
        else:
            return []
