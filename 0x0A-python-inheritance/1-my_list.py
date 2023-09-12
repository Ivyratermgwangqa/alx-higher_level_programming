#!/usr/bin/python3
class MyList(list):
    """Type class MyList  inherits print_sorted function"""

    def print_sorted(self):
        print(sorted(self))
