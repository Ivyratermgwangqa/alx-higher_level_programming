#!/usr/bin/python3

class Square:
    _side_len = 0

    def __init__(self, new_len=0):
        if type(new_len) is not int:
            raise TypeError('length must be an integer')
        if new_len < 0:
            raise ValueError('length must be >= 0')
        self._Square__side_len = new_len

    def area(self):
        return self._Square__side_len ** 2 
