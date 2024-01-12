#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    weighted_scores = 0
    divisor = 0

    for _tuple in my_list:
        weighted_scores += _tuple[0] * _tuple[1]
        divisor += _tuple[1]

    return weighted_scores / divisor
