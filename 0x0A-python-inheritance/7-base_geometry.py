#!/usr/bin/python3
"""
Module: my_module
This module defines the BaseGeometry class.

The BaseGeometry class provides a base structure for geometric objects.
"""


class BaseGeometry:
    """
    Type or class of BaseGeometry
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
