#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This is the class unittest for the max_integer function
    """

    def test_sorted_list(self):
        """
        Test when the input list is sorted in ascending order.
        """
       sorted_list = [1, 2, 3, 4]
       self.assertEqual(max_integer(sorted_list), 4)

    def test_unsorted_list(self):
        """
        Test when the input list is unsorted.
        """
        unsorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(unsorted_list), 4)

    def test_empty_list(self):
        """
        Test when the input list is empty.
        """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floatl(self):
        """
        Test when the input list contains floating-point numbers.
        """
        floatl = [1.25, 2.33, 3.67, 4.44]
        self.assertEqual(max_integer(floatl), 4.44)

    def test_intl_floatl(self):
        """
        Test when the input list contains a mix of integers and floating-point numbers.
        """
        intl_floatl = [1.25, 4.44, 4, 5]
        self.assertEqual(max_integer(intl_floatl), 5)

    def test_only_one(self):
        """
        Test when the input list contains only one element.
        """
        only_one = [7]
        self.assertEqual(max_integer(only_one), 7)

    def test_max_first(self):
        """
        Test when the maximum element is at the beginning of the list.
        """
        max_first = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_first), 4)

    def test_max_middle(self):
        """
        Test when the maximum element is in the middle of the list.
        """
        max_middle = [1, 2, 4, 3]
        self.assertEqual(max_integer(max_middle), 4)

    def test_non_string(self):
        """
        Test when the input is a non-string value.
        """
        self.assertEqual(max_integer(""), None)

    def test_many_strings(self):
        """
        Test when the input list contains strings.
        """
        many_strings = ["string1", "string2", "string3"]
        self.assertEqual(max_integer(many_strings), "string3")

if __name__ == '__main__':
    unittest.main()
