#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    truth_array = []

    for item in my_list:
        if item % 2 == 0:
            truth_array.append(True)
        else:
            truth_array.append(False)

    return truth_array
