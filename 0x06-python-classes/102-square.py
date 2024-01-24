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

    def __eq__(self, other):
        """Checks whether two squares are equal

            Args:
                param1 (Square): An instance of Square

            Returns:
                True if they are. False if they are not.
        """

        if self.area() == other.area():
            return True

        return False

    def __lt__(self, other):
        """Checks whether Square other is smaller than self

        Args:
            param1 (Square): An instance of Square

        Returns:
            True if other is smaller than self
        """

        if self.area() < other.area():
            return True

        return False

    def __gt__(self, other):
        """Checks whether Square self is greater than other

        Args:
            param1 (Square): An instance of Square

        Returns:
            True if self is greater than other
        """

        if self.area() > other.area():
            return True

        return False

    def __ge__(self, other):
        """Checks whether Square self is greater or equal than other

        Args:
            param1 (Square): An instance of Square

        Returns:
            True if self is greater or equal than other
        """

        if self.area() >= other.area():
            return True

        return False

    def __le__(self, other):
        """Checks whether Square self is less or equal than other

        Args:
            param1 (Square): An instance of Square

        Returns:
            True if self is less or equal than other
        """

        if self.area() <= other.area():
            return True

        return False
