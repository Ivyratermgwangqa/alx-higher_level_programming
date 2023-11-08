#!/usr/bin/python3
"""
Module: my_module
This module contains the 'load_from_json_file' function for reading.
The 'load_from_json_file' function takes a filename as input.
"""


import json


def load_from_json_file(filename):
    """
    Read a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file to be read.

    Returns:
        object: The Python object represented by JSON data the file.

    Notes:
        This function uses the 'json.load' method from the 'json'.
    """
    with open(filename) as f:
        return json.load(f)
