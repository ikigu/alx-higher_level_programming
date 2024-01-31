#!/usr/bin/python3

"""tests file"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests max area"""

    def test_zero_list_len(self):
        """tests some cases"""
        self.assertEqual(max_integer(), None)

    def test_correct_use(self):
        """test correct use"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
