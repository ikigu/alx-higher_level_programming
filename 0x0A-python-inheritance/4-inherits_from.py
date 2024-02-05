#!/usr/bin/python3

"""Checks if an object inherits from another"""


def inherits_from(obj, a_class):
    """
    Checks if obj inherits from a_class

    Args:
        obj (any): the object
        a_class (class): class to check against

    Return:
        True if obj inhertis from a_class;
        False otherwise
    """

    
    if type(obj).__name__ == a_class.__name__:
        return False
    elif issubclass(type(obj), a_class):
        return True

    return False
