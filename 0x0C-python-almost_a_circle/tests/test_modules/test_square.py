#!/usr/bin/python3
"""Unittest for Square"""

import unittest
from models.square import Square

class TestSquareMethods(unittest.TestCase):
    """Type class unittest instance for Square"""

    def test_is_instance(self):
        self.assertIsInstance(Square(10, 7), Square)

    def test_empty_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_is_instance_with_single_arg(self):
        self.assertIsInstance(Square(10), Square)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 7, 8, 2)._Square__size)

    def test_getter_size(self):
        sqr = Square(10, 7, 8, 2)
        self.assertEqual(10, sqr.size)

    def test_setter_size(self):
        sqr = Square(10, 7, 8, 2)
        sqr.size = 20
        self.assertEqual(20, sqr.size)

    def test_getter_height(self):
        sqr = Square(10, 7, 8, 2)
        sqr.size = 10
        self.assertEqual(10, sqr.height)

    def test_getter_y(self):
        self.assertEqual(0, Square(10).y)

    def test_getter_x(self):
        self.assertEqual(0, Square(10).x)

    def test_two_args(self):
        sqr = Square(10, 7)
        sqr2 = Square(4, 8)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_three_args(self):
        sqr = Square(10, 7, 2)
        sqr2 = Square(4, 8, 1)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_four_args(self):
        sqr = Square(10, 7, 2, 8)
        sqr2 = Square(4, 2, 1, 3)
        self.assertNotEqual(sqr.id, sqr2.id)

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Square(10, 7, 2, 8, 4, 1)

    def test_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 10)

    def test_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Edward", 10)

    def test_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(10.2, 7)

    def test_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 10, "b": 7}, 8)

    def test_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10, 7, 8], 8)

    def test_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 7, 8), 8)

    def test_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 10)

    def test_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 10)

    def test_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 7, 8}, 8)

    def test_size_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({10, 7, 8, 1}), 8)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10, 7)

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 7)

if __name__ == '__main__':
    unittest.main()
