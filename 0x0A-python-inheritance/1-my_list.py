#!/usr/bin/python3
"""
Module: my_module
This module contains a function for looking up the attributes and methods of an object.
"""
class MyList(list):
    """Type class MyList  inherits print_sorted function"""
    def print_sorted(self):
        print(sorted(self))
