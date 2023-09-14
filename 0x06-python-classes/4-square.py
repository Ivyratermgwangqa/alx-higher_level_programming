#!/usr/bin/python3

class Square:
    """
    Square represents a square with a side length.

    Attributes:
        _side_len (int): The side length of the square.
    """
    _side_len = 0

    def __init__(self, size=0):
         """
        Initializes a Square object with a specified side length.

        Args:
            size (int, optional): The side length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is a negative integer.
        """
        if type(new_size) is not int:
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

    @property
    def size(self):
         """
        Get the side length of the square.

        Returns:
            int: The side length of the square.
        """
        return self._Square__side_len

    @size.setter
    def size(self, value):
         """
        Set the side length of the square.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is a negative integer.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = value
