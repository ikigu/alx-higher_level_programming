#!/usr/bin/python3


"""Exact same object"""


def is_same_class(obj, a_class):
    """Checks if obj is of class a_class

    Args:
        obj (any): the object to check
        a_class: some class

    Return:
        True if object is exactly an instance of specified class;
        False otherwise
    """

    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
