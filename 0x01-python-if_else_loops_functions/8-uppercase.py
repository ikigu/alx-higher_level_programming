#!/usr/bin/python3

"""
Write a function that prints a string in uppercase followed by a new line.

-> Prototype: def uppercase(str):
-> You can only use no more than 2 print functions with string format
-> You can only use one loop in your code
-> You are not allowed to import any module
-> You are not allowed to use str.upper() and str.isupper()
-> Tips: ord()

"""


def uppercase(str):
    for i in range(0, len(str)):

        char_in_ascii = ord(str[i])

        if char_in_ascii > 96 and char_in_ascii < 123:
            char_in_ascii -= 32

        if i != len(str) - 1:
            print("{char:c}".format(char=char_in_ascii), end="")
        else:
            print("{char:c}".format(char=char_in_ascii))
