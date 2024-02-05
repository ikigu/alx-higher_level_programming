#!/usr/bin/python3

"""adds attribute to object"""


def add_attribute(obj, name, value):
    """adds attribute"""

    if hasattr(obj, "__dict__"):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
