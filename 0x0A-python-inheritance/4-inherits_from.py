#!/usr/bin/python3
"""
Module: my_module
This module contains a function for checking if an object inherited.
"""


def inherits_from(obj, a_class):
    """
    Function to check if an object is inherited in a class.
    Args:
    param1: obj
        The object to be checked.
    param2: a_class
        The class to check if 'obj' is inherited from.

    Returns:
    True if 'obj' is a subclass of 'a_class', otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
