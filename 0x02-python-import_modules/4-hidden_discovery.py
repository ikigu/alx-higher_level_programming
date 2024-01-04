#!/usr/bin/python3

import hidden_4


def print_names():
    names = dir(hidden_4)

    for name in names:
        if name[:2] != "__":
            print(name)


if __name__ == "__main__":
    print_names()
