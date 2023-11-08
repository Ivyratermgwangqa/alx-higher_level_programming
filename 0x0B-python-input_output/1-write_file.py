#!/usr/bin/python3
"""
Module: my_module
This module contains the 'write_file' function for writing a string.

The 'write_file' function writes a specified string to a text file.
"""


def write_file(filename="", text=""):
    """returns the num of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
