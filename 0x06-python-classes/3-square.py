#!/usr/bin/python3

class Square:
    _side_len = 0

    def __init__(self, new_len=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__side_len = size

        def area(self):
            return self._Square__side_len ** 2
