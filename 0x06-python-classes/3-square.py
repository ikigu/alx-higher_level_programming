#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            param1 (int, optional): The size of the side of the square.
        """

        self.size = size

    @property
    def size(self):
        """int: size of the side of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns:
            The area of the square
        """
        return self.size * self.size
