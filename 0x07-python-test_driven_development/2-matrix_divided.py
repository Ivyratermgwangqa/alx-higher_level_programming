#!/usr/bin/python3
"""
matrix_divided module
This module defines a function matrix_divided that divides all elements.

"""

def matrix_divided(matrix, div):
    """
    Divide all elements in a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix containing numeric values.
        div (int or float): The divisor to divide the matrix elements by.

    Returns:
        list of lists: A new matrix with the division calculated.

    Raises:
        TypeError: If the matrix is not a list of list.
        ZeroDivisionError: If the divisor (div) is zero.
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float))
                for row in matrix for element in row)):

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (int or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
