#!/usr/bin/python3
"""
Module: student
This module defines a Student class that represents a student.

The class provides a 'to_json' method to convert a Student object.
"""


class Student:
    """
    Representation of student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Get a dictionary representation of the Student.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        return self.__dict__
