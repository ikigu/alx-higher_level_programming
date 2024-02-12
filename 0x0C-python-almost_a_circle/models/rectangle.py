#!/usr/bin/python3

"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Creates Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiates the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __validate_integer(self, integer, attr_name):
        """validates that an attribute is an integer that meets certain reqs"""
        if type(integer) is not int:
            raise TypeError(f"{attr_name} must be an integer")

        if integer <= 0:
            if attr_name == 'width' or attr_name == 'height':
                raise ValueError(f"{attr_name} must be > 0")

        if integer < 0:
            if attr_name == 'x' or attr_name == 'y':
                raise ValueError(f"{attr_name} must be >= 0")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""

        self.__validate_integer(width, "width")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""

        self.__validate_integer(height, "height")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""

        self.__validate_integer(x, "x")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""

        self.__validate_integer(y, "y")
        self.__y = y

    def area(self):
        """Gets the area of the rectangle by multiplying width and height"""
        return self.__width * self.__height

    def display(self):
        """print out the object"""
        h = 0
        w = 0

        while h < self.__height:

            while w < self.__width:
                print("#", end="")
                w += 1

            print("")

            w = 0
            h += 1

    def __str__(self):
        """Return the string representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update the rectangle"""

        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif len(kwargs) > 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                else:
                    self.y = kwargs[key]
