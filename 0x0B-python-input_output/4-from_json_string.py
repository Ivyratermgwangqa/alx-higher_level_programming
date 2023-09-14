#!/usr/bin/python3
"""
Module: my_module
This module contains the 'from_json_string' function.

The 'from_json_string' function takes a JSON string as input.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object representation.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.

    Notes:
        This function uses the 'json.loads' method from the 'json'.
    """
    return json.loads(my_str)
