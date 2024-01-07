#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()

    if my_list:
        for number in my_list:
            print("{:d}".format(number))
