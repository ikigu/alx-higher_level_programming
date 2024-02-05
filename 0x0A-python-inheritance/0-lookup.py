#!/usr/bin/python3

"""Returns list of available attributes"""


def lookup(obj):
    """Returns list of attributes

    Args:
        obj (obj): The object whose attributes are returned

    Return:
        The list of attributes
    """

    return dir(obj)

