#!/usr/bin/python3

"""adds attribute to object"""


def add_attribute(obj, name, value):
    """adds attribute"""

    try:
        obj.__setattr__(name, value)
    except:
        raise TypeError("can't add new attribute")
