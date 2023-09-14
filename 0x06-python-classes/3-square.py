#!/usr/bin/python3
"""
Square represents a square with a side length.

Attributes:
    _side_len (int): The side length of the square.
"""


class Square:
    _side_len = 0

    def __init__(self, new_len=0):
        """
        Initializes a Square object with a specified side length.

        Args:
            size (int, optional): The side length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = size

        def area(self):
            """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
            return self._Square__side_len ** 2
