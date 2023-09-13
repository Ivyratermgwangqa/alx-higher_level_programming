#!/usr/bin/python3
"""
Module: my_module
This module contains the 'read_file' function for reading and printing.
The 'read_file' function reads a text file in UTF-8 encoding and prints.
"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
