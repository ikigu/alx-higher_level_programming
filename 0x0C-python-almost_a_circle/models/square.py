#!/usr/bin/python3


"""Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square initialize"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """width and height getter"""
        return self.width

    @size.setter
    def size(self, size):
        """width and height setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the rectangle"""

        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif len(kwargs) > 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                else:
                    self.y = kwargs[key]
