#!/usr/bin/python3
"""
Module: my_module
This module defines the BaseGeometry class.

The BaseGeometry class provides a base structure for geometric objects.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Type or class of Rectangle inherit BaseGeometry"""

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
