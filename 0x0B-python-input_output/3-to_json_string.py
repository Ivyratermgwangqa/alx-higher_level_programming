#!/usr/bin/python3
"""
Module: my_module
This module contains the 'to_json_string' function.

The 'to_json_string' function takes an object as input.
"""



import json

def to_json_string(my_obj):
    """
    Convert an object to a JSON string representa/tion.

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object as a string.

    Notes:
        This function uses the 'json.dumps' method from the 'json'.
    """
    return json.dumps(my_obj)
