#!/usr/bin/python3

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
        __str__(): Return a string representation of the Rectangle as a series of '#' characters.
        __repr__(): Return a string representation of the Rectangle that can be used to recreate the object.
        """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)
    
    def __str__(self):
    if self.width == 0 or self.height == 0:
        return ""
    else:
        rectangle_str = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle_str += "#"
            rectangle_str += "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
