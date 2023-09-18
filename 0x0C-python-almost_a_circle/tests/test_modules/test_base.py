#!/usr/bin/python3
"""Unittest for Base module"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os


class TestBaseInstances(unittest.TestCase):
    """Type class of testing for instances"""

    def test_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)
