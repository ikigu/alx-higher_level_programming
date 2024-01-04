#!/usr/bin/python3

import hidden_4


def print_names():
    names = dir(hidden_4)

    for i in range(0, len(names)):
        if names[i][0] != "__":
            print(names[i])


if __name__ == "__main__":
    print_names()
