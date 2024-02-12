#!/usr/bin/python3


"""Tests Base Class"""


import unittest
import models.base
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
