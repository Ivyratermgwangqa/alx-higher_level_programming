#!/usr/bin/python3
"""
Module: my_module
This module defines the Square class, which inherits from Rectangle.

The Square class represents a square geometric shape.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Type or class of square inherits a rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
