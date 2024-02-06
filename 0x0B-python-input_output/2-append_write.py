#!/usr/bin/python3

"""Appends text to file"""


def append_write(filename="", text=""):
    """Appends text to file"""

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
