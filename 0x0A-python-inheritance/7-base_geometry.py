#!/usr/bin/python3

"""Creates an empty class BaseGeometry"""


class BaseGeometry():
    """An empty class"""

    def area(self):
        """Raises an Exception that area is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0

        Args:
            name (str): name of value
            value (int): value
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
