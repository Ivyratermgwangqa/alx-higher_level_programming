#!/usr/bin/python3
"""
Module: my_module
This module defines the Rectangle class, which inherits from BaseGeometry.

The Rectangle class represents a geometric rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Type or class of Rectangle inherits BaseGeometry"""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string
