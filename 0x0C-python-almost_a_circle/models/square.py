#!/usr/bin/python3
""" Square Module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square instance """

        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """ Return a string representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width
                )

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter for size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update Square attributes """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Return the dictionary representation of a Square """
        dict = {}
        dict['id'] = self.id
        dict['size'] = self.width
        dict['x'] = self.x
        dict['y'] = self.y
        return dict
