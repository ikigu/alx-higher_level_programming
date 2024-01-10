#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return_matrix = []

    for _list in matrix:
        new_list = list(map(lambda x: x*x, _list))
        return_matrix.append(new_list)

    return (return_matrix)
