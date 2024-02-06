#!/usr/bin/python3

"""Creates a Student class"""


class Student():
    """Creates a Student"""

    def __init__(self, first_name, last_name, age):
        """Inits the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dict rep of Student instance"""

        return self.__dict__
