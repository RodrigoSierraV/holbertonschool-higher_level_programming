#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_nolist(self):
        """tests for no list"""
        self.assertIsNone(max_integer())

    def test_emptylist(self):
        """tests for empty list"""
        self.assertIsNone(max_integer([]))

    def test_typerr(self):
        """tests for type of the argument"""
        self.assertNotIsInstance(max_integer((2, 3)), list)

    def test_typecheck(self):
        """tests check for type of the result"""
        self.assertIsInstance(max_integer([2, 6, 80]), int)

    def test_string(self):
        """tests if a member of list isn't int"""
        with self.assertRaises(TypeError):
            max_integer([2, '6', 80])

    def test_dict(self):
        """tests when a dictionary is passed"""
        with self.assertRaises(KeyError):
            max_integer({'list': [2, 3, 80]})

    def test_ops(self):
        """tests when there is a math operation inside list"""
        self.assertEqual(max_integer([5*100, 3, 8, 11]), 500)

    def test_float(self):
        """tests when floats are passed"""
        self.assertEqual(max_integer([2.3, 450.857, 8, 11]), 450.857)

if __name__ == "__main__":
    unittest.main()
