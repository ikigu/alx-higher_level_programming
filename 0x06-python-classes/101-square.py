#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            param1 (int, optional): The size of the side of the square.
            param2 (tuple, optional): the position of the square
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """tuple: Position of the square."""
        return self.__position

    @position.setter
    def position(self, position):
        if (type(position) is not tuple or len(position) != 2 or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Returns:
            The area of the square
        """
        return self.size * self.size

    def __str__(self):
        """Prints the square with # characters

        Returns:
            A string to print
        """

        string = ""

        if self.size == 0:
            return string

        for _ in range(self.size):
            for _ in range(self.position[0]):
                string += " "
            for _ in range(self.size):
                string += "#"
            else:
                string += "\n"

        return string
