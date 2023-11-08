#!/usr/bin/python3
"""
Module: my_module
This module contains the 'append_write' function for appending a string.

The 'append_write' function appends a specified string to a text file.
"""


def append_write(filename="", text=""):
    """eturns the number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
