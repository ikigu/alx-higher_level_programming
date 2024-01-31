#!/usr/bin/python3

""" This module has a function that adds two integers"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        param1 (int | float): The first integer
        param2 (int | float): The second integer

    Returns:
        int: The sum of a and b
    """

    number = (int, float)

    if not isinstance(a, number):
        raise TypeError("a must be an integer")

    if not isinstance(b, number):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
