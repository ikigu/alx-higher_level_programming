#!/usr/bin/python3

"""Prints square of give size"""


def print_square(size):
    """prints square of given size

    Args:
        size (int): the length of one side of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for side in range(size):
            print('#', end="")

        if side < size:
            print('')
