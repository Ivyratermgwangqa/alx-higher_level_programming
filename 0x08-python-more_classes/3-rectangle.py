#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """
    This class represents a Rectangle.

    A Rectangle is defined by its width and height attributes.

    Attributes:
        width (int): The width of the Rectangle.
        height (int): The height of the Rectangle.

    Methods:
        area(): Calculate and return the area of the Rectangle.
        perimeter(): Calculate and return the perimeter of the Rectangle.
        __str__(): Return a string representation of the Rectangle.
        __repr__(): Return a string representation of the Rectangle.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        reg = []
        for i in range(self.__height):
            [reg.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                reg.append("\n")
        return ("".join(reg))
