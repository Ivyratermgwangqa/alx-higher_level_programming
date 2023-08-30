#!/usr/bin/python3

class Square:
    _side_len = 0

    def __init__(self, size=0):
        if type(new_size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = size

    def area(self):
        return self._Square__side_len ** 2

    @property
    def size(self):
        return self._Square__side_len

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = value
