#!/usr/bin/python3

"""
Write a function that prints the last digit of a number.

=> Prototype: def print_last_digit(number):
=> Returns the value of the last digit
=> You are not allowed to import any module

"""


def print_last_digit(number: int) -> int:
    copy_of_number = number

    if number < 0:
        copy_of_number *= -1

    last_digit = copy_of_number % 10

    print("{}".format(last_digit), end="")

    return last_digit
