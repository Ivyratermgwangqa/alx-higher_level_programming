#!/usr/bin/python3
"""Module for the Base class."""

import json
import csv
import turtle
import random


class Base:
    """Base class for managing objects."""

    _num_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object with an optional ID."""
        if id is not None:
            self.id = id
        else:
            Base._num_objects += 1
            self.id = Base._num_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a Python list or dictionary to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string): 
        """Convert a JSON string to a Python list or dictionary."""
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)
            
    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file."""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                data_list = cls.from_json_string(json_data)
                for item in data_list:
                    instance_list.append(cls.create(**item))
        except FileNotFoundError:
            pass
        return instance_list
        
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle."""
        turtle.setup(width=800, height=600)
        turtle.bgcolor("white")

        t = turtle.Turtle()
        t.shape("turtle")
        t.pensize(10)
        turtle.colormode(255)

        x, y = -355, -255
        max_height = 0
        column = 0

        for shape in list_rectangles + list_squares:
            t.pensize(0)
            random_color = (
                    random.randint(1, 254),
                    random.randint(1, 254),
                    random.randint(1, 254)
                    )

            t.color(random_color)

            t.goto(x, y)

            if shape.height > max_height:
                max_height = shape.height

            if x > 255:
                column += 1
                if column == 1:
                    y += max_height + 10
                    x -= shape.width + 10
                elif column == 2:
                    x = -355

            x += shape.width + 10
            t.pensize(10)

            for _ in range(2):
                t.lt(90)
                t.fd(shape.height)
                t.rt(90)
                t.fd(shape.width)
                t.rt(180)

            t.goto(x, y)

        turtle.exitonclick()
