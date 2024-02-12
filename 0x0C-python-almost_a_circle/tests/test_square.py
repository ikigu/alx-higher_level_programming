"""Tests square class"""


import unittest
from models.square import Square
import models.square
from io import StringIO
from unittest.mock import patch


class TestsquareClass(unittest.TestCase):
    def test_doc(self):
        self.assertTrue(len(Square.__doc__) > 1)
        self.assertTrue(len(models.square.__doc__) > 1)
        self.assertTrue(len(Square.__init__.__doc__) > 1)

    def test_square_attributes(self):
        s1 = Square(9, 7, 8)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 9)
        self.assertEqual(s1.width, s1.height)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)

        del s1

    def test_deletion(self):
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        del s1

        s2 = Square(2)
        self.assertEqual(s2.id, 1)
        del s2

    def test_no_attributes(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_str(self):
        r3 = Square(3, 4, 5)

        self.assertEqual(r3.__str__(), "[Square] (1) 4/5 - 3")

        del r3

    def test_integer_validation(self):
        with self.assertRaises(TypeError) as context:
            r1 = Square("9")
        self.assertEqual(context.exception.args[0], "width must be an integer")

    def test_size_getter_and_setter(self):
        r1 = Square(9)

        with self.assertRaises(TypeError) as context:
            r1.size = (2, 9)
        self.assertEqual(context.exception.args[0], "width must be an integer")

        r1.size = 98

        self.assertEqual(98, r1.size)
