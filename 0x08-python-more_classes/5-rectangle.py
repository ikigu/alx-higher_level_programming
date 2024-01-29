#!/usr/bin/python3

"""module creates a Rectangle class that does nothing"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initiates the rectangle

        Args:
            param1 (int): the width of the rectangle
            param2 (int): the height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of a Rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height of a Rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.height == 0 or self.width == 0:
            return 0

        return 2 * (self.height + self.width)

    def __str__(self):
        """returns a printable string"""

        to_print = ""

        if self.__height == 0 or self.__width == 0:
            return to_print

        for row in range(self.__height):
            for column in range(self.__width):
                to_print += '#'

            if self.__height > row + 1:
                to_print += '\n'

        return to_print

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """called when instance is deleted"""

        print("Bye rectangle...")
