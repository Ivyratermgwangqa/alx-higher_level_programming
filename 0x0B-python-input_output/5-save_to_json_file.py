#!/usr/bin/python3
"""
Module: my_module
This module contains the 'save_to_json_file' function.

The 'save_to_json_file' function takes a Python object.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a JSON file.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The path to the JSON file.

    Notes:
        This function uses the 'json.dump' method from the 'json'.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
