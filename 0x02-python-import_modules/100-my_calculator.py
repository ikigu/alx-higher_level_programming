#!/usr/bin/python3

from sys import argv, exit
from calculator_1 import mul, sub, div, add


def calculator():
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)

    operators = "-+*/"

    for operator in operators:
        if argv[2] == operator:
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))

    if argv[2] == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    if argv[2] == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    if argv[2] == '/':
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))


if __name__ == "__main__":
    calculator()
