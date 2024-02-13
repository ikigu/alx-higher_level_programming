#!/usr/bin/python3


"""Tests Base Class"""


import unittest
import models.base
import json
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Tests Base Class"""

    def test_docs(self):
        """Test docs for module, class and methods"""

        self.assertTrue(len(Base.__doc__) > 1)
        self.assertTrue(len(models.base.__doc__) > 1)
        self.assertTrue(len(Base.__init__.__doc__) > 1)

    def test_id(self):
        """Test id"""

        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        b5 = Base("id")

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, "id")

        del b1
        del b2
        del b3
        del b4
        del b5

    def test_json(self):
        """test json"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])

        self.assertEqual(
            dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json.loads(json_dictionary), [dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_empty_list_for_json(self):
        """test"""

        empty_string_array = Base.to_json_string(None)
        self.assertEqual("[]", empty_string_array)

        empty_string_array = Base.to_json_string([])
        self.assertEqual("[]", empty_string_array)

    # def test_wrong_types_to_json(self):
    #     with self.assertRaises(TypeError):
    #         Base.to_json_string({"t": "g"})

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file(None)

        with open("Rectangle.json", 'r', encoding='utf-8') as file:
            content = json.loads(file.read())
            expected = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {
                "y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
            self.assertTrue(content == expected)

        with open("Square.json", 'r', encoding='utf-8') as f:
            content = json.loads(f.read())
            expected = []
            self.assertTrue(content == expected)

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        json_list_input = Rectangle.to_json_string(list_input)
        list_from_json_string = Base.from_json_string(json_list_input)
        self.assertEqual(list_input, list_from_json_string)

        empty_list = Base.from_json_string(None)
        empty_list_also = Base.from_json_string("")

        self.assertEqual(empty_list, [])
        self.assertEqual(empty_list_also, [])

    def test_create(self):
        kwar = {"height": 9, "width": 2, "id": "bear", "x": 78, "y": 17}
        kwas = {"size": 8, "x": 8, "y": 4, "id": 18}

        s = Square.create(**kwas)
        r = Rectangle.create(**kwar)

        self.assertEqual(s.to_dictionary(), kwas)
        self.assertEqual(r.to_dictionary(), kwar)

    def test_load_from_file(self):
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        empty_rectangles = Rectangle.load_from_file()
        empty_squares = Square.load_from_file()

        self.assertEqual(empty_rectangles, [])
        self.assertEqual(empty_squares, [])

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(
            list_rectangles_output[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(
            list_rectangles_output[1].to_dictionary(), r2.to_dictionary())

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertEqual(
            list_squares_output[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(
            list_squares_output[1].to_dictionary(), s2.to_dictionary())


if __name__ == "__main__":
    unittest.main()
