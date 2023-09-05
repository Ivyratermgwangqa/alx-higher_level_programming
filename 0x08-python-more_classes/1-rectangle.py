#!/usr/bin/python3
"""
Class rectangle
"""

class Rectangle:
 """
    This class represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Calculate the area of the rectangle.
        perimeter(): Calculate the perimeter of the rectangle.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        def attributes(self):
            key_order = ['height', 'width']
            return {key: getattr(self, key) for key in key_order}

if __name__ == "__main__":
    pass
