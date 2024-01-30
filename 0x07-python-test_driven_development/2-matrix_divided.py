#!/usr/bin/python3

"""module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix

    Args:
        param1 (list): a matrix of ints or floats
        param2 (int | float): a divisor

    Returns:
        a new matrix, all elements have been divided by divisor
    """

    """matrix is not a list exception"""
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    """non-numbers in matrix exception"""
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])

    """rows in matrix are different lengths exception"""
    for row in matrix:
        if len(row) is not row_length:
            raise TypeError("Each row of the matrix must have the same size")

    """div is not a number exception"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """division by zero exception"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return_matrix = []

    for row in matrix:
        new_row = [round((element / div), 2) for element in row]
        return_matrix.append(new_row)

    return return_matrix
