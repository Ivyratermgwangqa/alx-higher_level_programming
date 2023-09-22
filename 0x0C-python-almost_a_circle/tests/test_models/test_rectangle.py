#!/usr/bin/python3
"""Unittest for Rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def setUp(self):
        Base._Base__nb_objects = 0  # Reset the base class attribute

    def test_is_instance(self):
        self.assertIsInstance(Rectangle(10, 7), Rectangle)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_private_width(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        with self.assertRaises(AttributeError):
            print(rec._Rectangle__width)

    def test_getter_width(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(10, rec.width)

    def test_setter_width(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.width = 20
        self.assertEqual(20, rec.width)

    def test_private_height(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        with self.assertRaises(AttributeError):
            print(rec._Rectangle__height)

    def test_getter_height(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(7, rec.height)

    def test_setter_height(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.height = 15
        self.assertEqual(15, rec.height)

    def test_private_y(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        with self.assertRaises(AttributeError):
            print(rec._Rectangle__y)

    def test_getter_y(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_setter_y(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)

    def test_private_x(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        with self.assertRaises(AttributeError):
            print(rec._Rectangle__x)

    def test_getter_x(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_setter_x(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_single_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_args(self):
        rec = Rectangle(10, 7)
        rec2 = Rectangle(4, 8)
        self.assertNotEqual(rec.id, rec2.id)

    def test_three_args(self):
        rec = Rectangle(10, 7, 2)
        rec2 = Rectangle(4, 8, 1)
        self.assertNotEqual(rec.id, rec2.id)

    def test_four_args(self):
        rec = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(4, 2, 1, 3)
        self.assertNotEqual(rec.id, rec2.id)

    def test_five_args(self):
        rec = Rectangle(10, 7, 2, 8, 4)
        rec2 = Rectangle(4, 2, 1, 3, 7)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 7, 2, 8, 4, 1)

    def test_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Edward", 10)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.2, 7)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 10, "b": 7}, 8)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10, 7, 8], 8)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((10, 7, 8), 8)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 10)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({10, 7, 8}, 8)

    def test_width_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({10, 7, 8, 1}), 8)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 7)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7)

if __name__ == '__main__':
    unittest.main()
