"""Tests square class"""


import unittest
from models.square import Square
import models.square
from io import StringIO
from unittest.mock import patch


class TestsquareClass(unittest.TestCase):
    def test_doc(self):
        """Test documentation"""
        self.assertTrue(len(Square.__doc__) > 1)
        self.assertTrue(len(models.square.__doc__) > 1)
        self.assertTrue(len(Square.__init__.__doc__) > 1)

    def test_square_attributes(self):
        """Test attributes"""
        s1 = Square(9, 7, 8)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.height, 9)
        self.assertEqual(s1.width, s1.height)
        self.assertEqual(s1.x, 7)
        self.assertEqual(s1.y, 8)

        del s1

    def test_deletion(self):
        """Test deletion"""
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        del s1

        s2 = Square(2)
        self.assertEqual(s2.id, 1)
        del s2

    def test_no_attributes(self):
        """Test no attributes"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_str(self):
        """test __str__"""
        r3 = Square(3, 4, 5)

        self.assertEqual(r3.__str__(), "[Square] (1) 4/5 - 3")

        del r3

    def test_integer_validation(self):
        """Test validation"""
        with self.assertRaises(TypeError) as context:
            r1 = Square("9")
        self.assertEqual(context.exception.args[0], "width must be an integer")

    def test_size_getter_and_setter(self):
        r1 = Square(9)

        with self.assertRaises(TypeError) as context:
            r1.size = (2, 9)
        self.assertEqual(context.exception.args[0], "width must be an integer")
        with self.assertRaises(ValueError) as context:
            r1.size = -98
        self.assertEqual(context.exception.args[0], "width must be > 0")
        with self.assertRaises(ValueError) as context:
            r1.size = 0
        self.assertEqual(context.exception.args[0], "width must be > 0")

        r1.size = 98

        self.assertEqual(98, r1.size)

    def test_update_0(self):
        """Test update"""
        r1 = Square(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Square] (10) 10/10 - 10")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 10")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 2")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Square] (89) 3/10 - 2")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Square] (89) 3/4 - 2")

        del r1

    def test_kwargs(self):
        r1 = Square(10, 10, 10, 10)

        r1.update(89, 3, x=9)
        self.assertEqual(r1.__str__(), "[Square] (89) 10/10 - 3")

        r1.update(x=9)
        self.assertEqual(r1.__str__(), "[Square] (89) 9/10 - 3")

        r1.update(id=987)
        self.assertEqual(r1.__str__(), "[Square] (987) 9/10 - 3")

        r1.update(y=987)
        self.assertEqual(r1.__str__(), "[Square] (987) 9/987 - 3")

        r1.update(214, 67, 738, 3)
        self.assertEqual(r1.__str__(), "[Square] (214) 738/3 - 67")

        del r1

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1, 9)
        s2 = Square(2, 2)
        s1_todict = s1.to_dictionary()

        self.assertEqual(
            s1_todict, {'id': 9, 'size': 10, 'x': 2, 'y': 1})
        self.assertEqual(s2.__str__(), "[Square] (1) 2/0 - 2")
        self.assertEqual(type(s1_todict), dict)

        s2.update(**s1_todict)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)
        self.assertEqual(s1_todict, s2.to_dictionary())

        del s1
        del s2
