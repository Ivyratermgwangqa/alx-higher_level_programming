#!/usr/bin/python3

class Rectangle:
    """
    This class represents a Rectangle.

    A Rectangle is defined by its width and height attributes.

    Attributes:
        width (int): The width of the Rectangle.
        height (int): The height of the Rectangle.
        number_of_instances (int): Count of num of Rectangle instances created.
        print_symbol (str): Symbol used to represent Rectangle when printing.

    Methods:
        area(): Calculate and return the area of the Rectangle.
        perimeter(): Calculate and return the perimeter of the Rectangle.
        __str__(): Return a string representation of the Rectangle
        __repr__(): Return a string representation of the Rectangle.
        __del__(): Destructor method that decrements the count of instances.
        bigger_or_equal(rect_1, rect_2): Compare two Rectangle instances.
        square(cls, size): Create square Rectangle instance with given size.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    rectangle_str += str(self.print_symbol)
                rectangle_str += "\n"
            return rectangle_str[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
