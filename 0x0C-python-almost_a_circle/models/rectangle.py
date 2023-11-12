#!/usr/bin/python3
"""Module of rectangle"""

import csv
from models.base import Base


class Rectangle(Base):
    """Type class of a rectangle inherited from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save a list of Rectangle instances to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["id", "width", "height", "x", "y"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for rect in list_objs:
                writer.writerow({
                    "id": rect.id,
                    "width": rect.width,
                    "height": rect.height,
                    "x": rect.x,
                    "y": rect.y
                })

    @classmethod
    def load_from_file_csv(cls):
        """ Load a list of Rectangle instances from a CSV file """
        filename = cls.__name__ + ".csv"
        rectangles = []
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    rect = cls(0, 0)
                    for key, value in row.items():
                        setattr(rect, key, int(value))
                    rectangles.append(rect)
        except FileNotFoundError:
            pass
        return rectangles

    def area(self):
        """Calculate area"""
        return self.width * self.height

    def display(self):
        """Display the Rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of the Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle's attributes"""

        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary function"""

        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x,
            "y": self.y,
            }
