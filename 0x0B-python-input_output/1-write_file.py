#!/usr/bin/python3

"""Function that writes a string to a text file
and returns the number of characters written"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)

        return chars_written
