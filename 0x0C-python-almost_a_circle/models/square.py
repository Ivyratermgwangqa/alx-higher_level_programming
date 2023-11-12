#!/usr/bin/python3
""" Square Module """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square instance """

        super().__init__(size, size, x, y, id)

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save a list of Square instances to a CSV file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for square in list_objs:
                writer.writerow({
                    "id": square.id,
                    "size": square.size,
                    "x": square.x,
                    "y": square.y
                })

    @classmethod
    def load_from_file_csv(cls):
        """ Load a list of Square instances from a CSV file """
        filename = cls.__name__ + ".csv"
        squares = []
        try:
            with open(filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    square = cls(0)
                    for key, value in row.items():
                        setattr(square, key, int(value))
                    squares.append(square)
        except FileNotFoundError:
            pass
        return squares

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
        square_dict = {}
        square_dict['id'] = self.id
        square_dict['size'] = self.width
        square_dict['x'] = self.x
        square_dict['y'] = self.y
        return square_dict
