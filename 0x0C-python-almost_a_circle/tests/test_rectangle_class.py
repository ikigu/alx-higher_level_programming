"""Tests Rectangle class"""


import unittest
from models.rectangle import Rectangle
import models.rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleClass(unittest.TestCase):
    """Tests Rectangle Class"""

    def test__doc(self):
        """Verify that module, class and methods are documented"""

        self.assertTrue(len(models.rectangle.__doc__) > 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 1)
        self.assertTrue(len(Rectangle.__doc__) > 1)
        self.assertTrue(len(Rectangle.area.__doc__) > 1)
        self.assertTrue(len(Rectangle.display.__doc__) > 1)
        self.assertTrue(len(Rectangle.update.__doc__) > 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 1)
        self.assertTrue(len(Rectangle.height.__doc__) > 1)
        self.assertTrue(len(Rectangle.width.__doc__) > 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 1)

    def test_id(self):
        """Rectangle 1"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(37, 14)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(14, 7)
        r5 = Rectangle(13, 45, 55, 6, "Bread")

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r5.id, "Bread")

        del r1
        del r2
        del r3
        del r4
        del r5

    def test_integer_validation(self):
        """Test string attributes"""
        with self.assertRaises(TypeError) as context:
            Rectangle("10", 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle(10, "5")
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle("10", "5")
        self.assertTrue(
            context.exception.args[0] == "width must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 6, "7", 8)
        self.assertTrue(
            context.exception.args[0] == "x must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 6, 7, "8")
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle({"10": "n"}, "5")
        self.assertTrue(
            context.exception.args[0] == "width must be an integer"
        )

        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, {7, 9}, 9)
        self.assertTrue(
            context.exception.args[0] == "x must be an integer"
        )

        # 0 or less than 0
        with self.assertRaises(ValueError) as context:
            Rectangle(0, 5, 4, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be > 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(-1, 5, 4, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be > 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(1, -1, 5, 5)
        self.assertTrue(
            context.exception.args[0] == "height must be > 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 0, 5, 5)
        self.assertTrue(
            context.exception.args[0] == "height must be > 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, -67, 5)
        self.assertTrue(
            context.exception.args[0] == "x must be >= 0"
        )
        with self.assertRaises(ValueError) as context:
            Rectangle(1, 1, 5, -5)
        self.assertTrue(
            context.exception.args[0] == "y must be >= 0"
        )

    def test_dict_attributes(self):
        """Test dict"""
        with self.assertRaises(TypeError) as context:
            Rectangle({"10": "n"}, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, {"5": "3"})
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, {"5": "4"})
        self.assertTrue(
            context.exception.args[0] == "x must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, {"5": "4"})
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

    def test_tuple_attributes(self):
        """Test Tuple attributes"""
        with self.assertRaises(TypeError) as context:
            Rectangle((1, 3), 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, (1, 3))
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, (1, 3))
        self.assertTrue(
            context.exception.args[0] == "x must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, (1, 3))
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

    def test_float_attributes(self):
        """Test float attributes"""
        with self.assertRaises(TypeError) as context:
            Rectangle(1.3, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 1.3)
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, 1.3)
        self.assertTrue(
            context.exception.args[0] == "x must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, 1.3)
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

    def test_bool_attributes(self):
        """Test bool attributes"""
        with self.assertRaises(TypeError) as context:
            Rectangle(True, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, False)
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, True)
        self.assertTrue(
            context.exception.args[0] == "x must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, False)
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

    def test_none_attributes(self):
        """Test NoneType"""
        with self.assertRaises(TypeError) as context:
            Rectangle(None, 5)
        self.assertTrue(
            context.exception.args[0] == "width must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, None)
        self.assertTrue(
            context.exception.args[0] == "height must be an integer"
        )
        with self.assertRaises(TypeError) as context:
            Rectangle(4, 5, None)
        self.assertTrue(
            context.exception.args[0] == "x must be an integer")

        with self.assertRaises(TypeError) as context:
            Rectangle(10, 5, 3, None)
        self.assertTrue(
            context.exception.args[0] == "y must be an integer"
        )

    def test_rectangle_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(7, 8)
        r3 = Rectangle(8990, 456)
        r4 = Rectangle(78, 3, 12, 4, 7)

        self.assertEqual(r1.area(), 3 * 2)
        self.assertEqual(r2.area(), 7 * 8)
        self.assertEqual(r3.area(), 8990 * 456)
        self.assertEqual(r4.area(), 78 * 3)

        del r1
        del r2
        del r3
        del r4

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stdout):
        """Test task 5"""

        r1 = {"output": Rectangle(1, 1), "expected": "#\n"}
        r2 = {"output": Rectangle(2, 3), "expected": "#\n##\n##\n##\n"}
        r3 = {"output": Rectangle(4, 5),
              "expected": "#\n##\n##\n##\n####\n####\n####\n####\n####\n"}

        r1["output"].display()
        self.assertEqual(stdout.getvalue(), r1["expected"])

        r2["output"].display()
        self.assertEqual(stdout.getvalue(), r2["expected"])

        r3["output"].display()
        self.assertEqual(stdout.getvalue(), r3["expected"])

        del r1
        del r2
        del r3

    def test_print(self):
        """Test task 6"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

        del r1
        del r2

    def test_update_0(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        del r1

    def test_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89, 3, height=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 3/10")

        r1.update(height=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 3/9")

        r1.update(x=19)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 19/10 - 3/9")

        r1.update(id=987)
        self.assertEqual(r1.__str__(), "[Rectangle] (987) 19/10 - 3/9")

        r1.update(y=987)
        self.assertEqual(r1.__str__(), "[Rectangle] (987) 19/987 - 3/9")

        r1.update(214, 67, 738, 3, 21)
        self.assertEqual(r1.__str__(), "[Rectangle] (214) 3/21 - 67/738")

        del r1

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(2, 2)
        r1_todict = r1.to_dictionary()

        self.assertEqual(
            r1_todict, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 2/2")
        self.assertEqual(type(r1_todict), dict)

        r2.update(**r1_todict)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1_todict, r2.to_dictionary())

        del r1
        del r2


if __name__ == "__main__":
    unittest.main()
