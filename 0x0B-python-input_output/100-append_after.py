#!usr/bin/python3
"""
Module: file_insertion
This module defines a function for inserting text.

The function 'append_after' reads the content of a text file.
Usage:
    To use the 'append_after' function, provide the filename.

Example:
    append_after("my_file.txt", "search_string", "new_text_to_insert")

This will modify 'my_file.txt' by inserting "new_text_to_insert".
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after matching lines.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
