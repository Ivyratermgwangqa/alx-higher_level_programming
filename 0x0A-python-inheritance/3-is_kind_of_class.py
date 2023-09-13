#!/usr/bin/python3
"""
Module: my_module
This module contains function for checking if object belongs to subclass.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object belongs to the same class or a subclass.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with the object's type.

    Returns:
        True if 'obj' is instance of 'a_class' or a subclass, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
