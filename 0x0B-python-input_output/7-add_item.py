#!/usr/bin/python3

"""adds arguments to python list then saves them to file"""


import sys


def add_args():
    """adds args to file"""

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    try:
        obj = load_from_json_file('add_item.json')
    except FileNotFoundError:
        obj = []

    for i in range(1, len(sys.argv)):
        obj.append(sys.argv[i])

    save_to_json_file(obj, 'add_item.json')


if __name__ == "__main__":
    add_args()
