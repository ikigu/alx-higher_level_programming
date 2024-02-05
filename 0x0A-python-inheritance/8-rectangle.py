#!/usr/bin/python3

"""Creates a Rectangle class that inherits from  BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates Rectangle class"""

    def __init__(self, width, height):
        """Initiates a rectangle"""
        try:
            self.integer_validator("width", width)
        finally:
            self.__width = width

        try:
            self.integer_validator("height", height)
        finally:
            self.__height = height
