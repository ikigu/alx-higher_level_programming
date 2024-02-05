#!/usr/bin/python3

""" Prints a sorted list"""


class MyList(list):
    """Creates a list based on list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        list_cp = self[:]
        list_cp.sort()
        print(list_cp)
