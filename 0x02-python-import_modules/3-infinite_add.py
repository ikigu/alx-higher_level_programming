#!/usr/bin/python3

from sys import argv

""" Infinite addition

Write a program that prints the result of the addition of all arguments

=> The output should be the result of the addition of all arguments,
   followed by a new line
=> You can cast arguments into integers by using int() 
   (you can assume that all arguments can be casted into integers)
=> Your code should not be executed when imported
"""


def add_args():
    sum = 0

    for i in range(1, len(argv)):
        sum += int(argv[i])

    print(sum)


if __name__ == "__main__":
    add_args()
