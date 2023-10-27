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
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result
