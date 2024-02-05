#!/usr/bin/python3

"""Creates a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates Square class, inheriting from Rectangle"""

    def __init__(self, size):
        try:
            self.integer_validator("size", size)
        finally:
            self.__size = size

        super().__init__(size, size)
