#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0 and len(matrix) == 1:
        print("")

    for list in matrix:
        for i in range(0, len(list)):
            if i < len(list) - 1:
                print("{:d}".format(list[i]), end=" ")
            else:
                print("{:d}".format(list[i]))
