#!/usr/bin/python3
"""
Module: my_module
This module contains a function for looking up the attributes and methods of an object.
"""
def lookup(obj):
    """Return list of obj"""
    return (dir(obj))
