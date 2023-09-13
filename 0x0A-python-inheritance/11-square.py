#!/usr/bin/python3
"""
Module: my_module
This module defines the MyInt class, which inherits from the int type.
MyInt overrides the equality and inequality operators to provide custom behavior.

"""


class MyInt(int):
    """
    Type class of MyInt inherit int type
    """

    def __eq__(self, other):
        return self.real != other

    def __ne__(self, other):
        return self.real == other
