#!/usr/bin/python3
"""
text_indentation module
Function that prints a text with new lines after using '.?:'
"""

def text_indentation(text):
    """
    Print text with 2 new lines after using '.?:'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end='')
        if text[i] == '\n' or text[i] in ".?:":
            if text[i] in ".?:":
                print('\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
