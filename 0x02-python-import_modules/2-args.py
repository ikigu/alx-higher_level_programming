#!/usr/bin/python3

from sys import argv


def print_args():
    number_of_args: int = len(argv) - 1
    print(number_of_args, end=" ")

    if number_of_args == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if number_of_args == 0:
        print(".")
        return
    else:
        print(":")

    for i in range(1, len(argv)):
        print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    print_args()
