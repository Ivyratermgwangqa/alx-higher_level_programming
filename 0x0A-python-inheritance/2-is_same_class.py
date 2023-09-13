#!/usr/bin/python3
"""
Module: my_module
This module contains a function for checking if an object is an instance.
"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a specified class.
    Args:
        obj: The object to be checked.
        a_class: The class to compare with the object's type.

    Returns:
        True if 'obj' is an instance of 'a_class', otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
