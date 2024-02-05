#!/usr/bin/python3

"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """Checks whether Same class or inherit from

    Args:
        obj (any): a random object
        a_class (class): class to test against

    Return:
        True if obj is instance or subclass of a_class;
        False otherwise
    """

    if isinstance(obj, a_class):
        return True

    return False
