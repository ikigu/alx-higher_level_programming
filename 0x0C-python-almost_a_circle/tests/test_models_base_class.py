#!/usr/bin/python3


"""Tests Base Class"""


import unittest
import models.base
from models.base import Base
from models.rectangle import Rectangle
import json


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


if __name__ == "__main__":
    unittest.main()
