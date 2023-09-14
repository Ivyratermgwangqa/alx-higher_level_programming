#!/usr/bin/python3
"""
Module: class_to_json
This module contains a function for converting an object.

The function 'class_to_json' returns a dictionary description.
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation suitable.

    Args:
        obj: The object to be converted to a JSON-compatible dictionary.

    Returns:
        dict: A dictionary description of the object's attributes and values.
    """
    return obj.__dict__
