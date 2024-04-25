#!/usr/bin/python3

"""
Finds the peak
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers

    Args:
        list_of_integers (list): The list of unsorted integers

    Return:
        The peak in the list of unsorted integers
    """

    if type(list_of_integers) is not list:
        return None

    if len(list_of_integers) == 0:
        return None

    for i in range(0, len(list_of_integers)):
        if i - 1 != -1:
            try:
                if list_of_integers[i] > list_of_integers[i + 1]:
                    if list_of_integers[i] > list_of_integers[i - 1]:
                        return list_of_integers[i]
            except IndexError:
                return list_of_integers[i]

    last_index = len(list_of_integers) - 1

    if len(list_of_integers) > 1:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]

    if (list_of_integers[last_index] > list_of_integers[last_index - 1]):
        return list_of_integers[len(list_of_integers) - 1]

    return None
