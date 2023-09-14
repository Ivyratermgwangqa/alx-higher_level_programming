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
            new_len (int, optional): The side length of the square.

        Raises:
            TypeError: If new_len is not an integer.
            ValueError: If new_len is a negative integer.
        """
        if type(new_len) is not int:
            raise TypeError('size must be an integer')
        if new_len < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = new_len
