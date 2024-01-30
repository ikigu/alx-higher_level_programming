#!/usr/bin/python3

"""Module prints given name"""


def say_my_name(first_name, last_name=""):
    """prints given name

    Args:
        param1 (str): first name
        param2 (str): second name

    Returns:
        Nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
