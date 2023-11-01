#!/usr/bin/python3
"""Module to find the max integer in a list

This module provides a function to find and return the maximum integer in a
list of integers.

"""

def max_integer(list=[]):
    """Find and return the maximum integer in a list of integers.

    Args:
        list (list): The input list of integers.

    Returns:
        int: The maximum integer in the list. Returns None if the list is empty.

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
