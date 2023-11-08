#!/usr/bin/python3
"""
Module: student
This module defines a Student class that represents a student.

The class provides a 'to_json' method to convert a Student object to a dictionary.

Example:
    student = Student("John", "Doe", 25)
    json_data = student.to_json()

    Output:
        {'first_name': 'John', 'last_name': 'Doe', 'age': 25}
"""

class Student:
    """
    Represents a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include in the dictionary.
                If not provided, all attributes are included.

        Returns:
            dict: A dictionary representing the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from a JSON dictionary.

        Args:
            json (dict): A dictionary where keys represent attribute names, and values represent
                the new values for those attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
