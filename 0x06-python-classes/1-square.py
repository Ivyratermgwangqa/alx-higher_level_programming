#!/usr/bin/python3

class Square:
    """
    Square represents a square with a side length.

    Attributes:
        _side_len (int): The side length of the square.
    """
    _side_len = 0

    def __init__(self, new_len=0):
        """
        Initializes a Square object with a specified side length.

        Args:
            new_len (int, optional): The side length of the square. Defaults to 0.
        """
        if new_len is not None:
            self._Square__side_len = new_len
