#!/usr/bin/python3

"""
This function will prints all possible combinations of two digits
Enforce the following:

-> Numbers must be separated by "," followed by space
-> 01 and 10 are considered the same combo
-> print only the smallest combo of two digits
-> No more than 3 print functions
-> No more than 2 loops
-> No variables
-> No modules
"""


for x in range(0, 10):
    for y in range(0, 10):
        if x == 8 and y == 9:
            print("{x:d}{y:d}".format(x=x, y=y))
        elif x != y and y > x:
            print("{x:d}{y:d}".format(x=x, y=y), end=", ")
