#!/usr/bin/python3

"""Creates a Student class"""


class Student():
    """Creates a Student"""

    def __init__(self, first_name, last_name, age):
        """Inits the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict rep of Student instance"""

        if attrs is None:
            return self.__dict__

        if len(attrs) > 0:
            _dict = {}

            for attr in attrs:
                try:
                    _dict[attr] = self.__dict__[attr]
                except KeyError:
                    pass

            return _dict
