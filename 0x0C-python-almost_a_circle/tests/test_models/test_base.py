#!/usr/bin/python3
"""Unittest for Base module"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseInstances(unittest.TestCase):

    def test_base_instances_with_none(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_base_instances_with_empty(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_base_single_id(self):
        self.assertEqual(5, Base(5).id)

    def test_base_public_id(self):
        public_b = Base(5)
        public_b.id = 10
        self.assertEqual(10, public_b.id)

    def test_base_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(5).__nb_instances)

    def test_base_str_id(self):
        self.assertEqual("tequila", Base("tequila").id)

    def test_base_float_id(self):
        self.assertEqual(3.1, Base(3.1).id)

    def test_base_dict_id(self):
        self.assertEqual({"val1": 1, "val2": 2}, Base({"val1": 1, "val2": 2}).id)

    def test_base_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_base_tuple_id(self):
        self.assertEqual((1, 2, 3), Base((1, 2, 3)).id)

    def test_base_nan_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_base_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_base_two_arguments(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_base_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_base_frozen_id(self):
        self.assertEqual(frozenset({"a", "b", "c"}), Base(frozenset({"a", "b", "c"})).id)

class TestBaseToJson(unittest.TestCase):

    def test_base_to_json_with_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_base_to_json_with_empty_list(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_base_to_json_with_type_error(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_base_to_json_with_extra_argument(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 10)

    def test_base_to_json_with_rectangle_type(self):
        rec = Rectangle(10, 7, 2, 8)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_base_to_json_with_square_type(self):
        sqr = Square(10, 2, 1)
        self.assertEqual(str, type(Base.to_json_string([sqr.to_dictionary()])))

    def test_base_to_json_with_rectangle_dict(self):
        rec = Rectangle(10, 7, 2, 8)
        self.assertTrue(len(Base.to_json_string([rec.to_dictionary()])))

    def test_base_to_json_with_square_dict(self):
        sqr = Square(10, 2, 1)
        self.assertTrue(len(Base.to_json_string([sqr.to_dictionary()])))

    def test_base_to_json_with_multiple_rectangle_dicts(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4, 6)
        list_dicts = [rec1.to_dictionary(), rec2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

    def test_base_to_json_with_multiple_square_dicts(self):
        sqr1 = Square(10, 2, 1)
        sqr2 = Square(7, 9)
        list_dicts = [sqr1.to_dictionary(), sqr2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)))

class TestBaseFromJson(unittest.TestCase):

    def test_base_from_json_with_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_base_from_json_with_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_base_from_json_with_type_error(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_base_from_json_with_extra_argument(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)

    def test_base_from_json_with_rectangle_type(self):
        linput = [{"id": 89, "width": 10, "height": 4}]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(list, type(loutput))

    def test_base_from_json_with_rectangle_dict(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2}]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_base_from_json_with_square_dict(self):
        linput = [{"id": 89, "size": 10, "height": 4}]
        json_linput = Square.to_json_string(linput)
        loutput = Square.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_base_from_json_with_multiple_rectangle_dicts(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2, "y": 1},
                  {"id": 7, "width": 1, "height": 7, "x": 8, "y": 2}
        ]
        json_linput = Rectangle.to_json_string(linput)
        loutput = Rectangle.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

    def test_base_from_json_with_multiple_square_dicts(self):
        linput = [{"id": 89, "width": 10, "height": 4, "x": 2, "y": 1},
                  {"id": 7, "width": 1, "height": 7, "x": 8, "y": 2}
        ]
        json_linput = Square.to_json_string(linput)
        loutput = Square.from_json_string(json_linput)
        self.assertEqual(linput, loutput)

class TestBaseSaveFile(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_file_with_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_file_with_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_file_with_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_file_with_extra_argument(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 10)

    def test_save_file_with_rectangle_type(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_with_square_type(self):
        sqr = Square(10, 2, 1)
        Square.save_to_file([sqr])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_with_multiple_rectangle_types(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(7, 2, 1, 4, 6)
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()))

    def test_save_file_with_multiple_square_types(self):
        sqr1 = Square(10, 2, 1, 8)
        sqr2 = Square(80, 10, 4, 2)
        Square.save_to_file([sqr1, sqr2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()))

class TestBaseLoadFile(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_file_with_empty(self):
        load = Rectangle.load_from_file()
        self.assertEqual([], load)

    def test_load_file_with_type_error(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 10)

    def test_load_file_with_rectangle_type(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec), str(load[0]))

    def test_load_file_with_square_type(self):
        sqr = Square(10, 2, 1, 8)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertEqual(str(sqr), str(load[0]))

    def test_load_file_with_type_check_rectangle(self):
        rec = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([rec])
        load = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in load))

    def test_load_file_with_type_check_square(self):
        sqr = Square(10, 2, 1, 8)
        Square.save_to_file([sqr])
        load = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in load))

    def test_load_file_with_rectangle_copy(self):
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(10, 2, 1, 4, 6)
        Rectangle.save_to_file([rec1, rec2])
        load = Rectangle.load_from_file()
        self.assertEqual(str(rec1), str(load[0]))

    def test_load_file_with_square_copy(self):
        sqr1 = Square(10, 7, 2, 8)
        sqr2 = Square(10, 2, 1, 8)
        Square.save_to_file([sqr1, sqr2])
        load = Square.load_from_file()
        self.assertEqual(str(sqr1), str(load[0]))

if __name__ == '__main__':
    unittest.main()
