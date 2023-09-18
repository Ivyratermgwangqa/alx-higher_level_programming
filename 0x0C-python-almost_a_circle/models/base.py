#!/usr/bin/python3
"""Module for the Base class."""

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
