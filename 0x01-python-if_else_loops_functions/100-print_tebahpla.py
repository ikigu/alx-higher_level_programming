#!/usr/bin/python3

def print_alpha(number: int):
    turn = 1

    while(number > 64 and number != 96):
        if turn == 1:
            print("{char:c}".format(char=number), end="")
            number = (number - 32) - 1
            turn = 2
        elif turn == 2:
            print("{char:c}".format(char=number), end="")
            number = (number + 32) - 1
            turn = 1

print_alpha(122)
