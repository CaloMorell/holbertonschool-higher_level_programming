#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..]).
    """

    def test_list(self):
        """Test a normal list.
        """
        result = max_integer([2, 3, 4, 4, 5, 5, 4, 21, 4342])
        self.assertEqual(result, 4342)

    def test_negative_list(self):
        """Test a negative normal list.
        """
        result = max_integer([-1, -2, -3, -4, -5, -7])
        self.assertEqual(result, -1)

    def test_list_one(self):
        """Test a list with only one element.
        """
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_list_same(self):
        """Test a list with arguments with the same value.
        """
        result = max_integer([0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_int(self):
        """Test a integer.
        """
        with self.assertRaises(Exception):
            max_integer(1)

    def test_float(self):
        """Test a float.
        """
        with self.assertRaises(Exception):
            max_integer(34.45)

    def test_boolean(self):
        """Test a boolean.
        """
        with self.assertRaises(Exception):
            max_integer(True)

    def test_string(self):
        """Test a string.
        """
        result = max_integer("sad")
        self.assertRaises(Exception, result)

    def test_tuple(self):
        """Test a tuple.
        """
        result = max_integer((2, 3))
        self.assertRaises(Exception, result)

    def test_dict(self):
        """Test a dictionary.
        """
        result = max_integer({})
        self.assertRaises(Exception, result)

    def test_void(self):
        """Test a function without parameters.
        """
        with self.assertRaises(Exception):
            max_integer(None)

    def test_float_list(self):
        """Test a list of floats.
        """
        result = max_integer([0.2, 3.2])
        self.assertRaises(Exception, result)

    def test_none_list(self):
        """Test a list with None value.
        """
        result = max_integer([None])
        self.assertRaises(Exception, result)

    def test_string_list(self):
        """Test a list with string values.
        """
        result = max_integer(["hola", "como", "vamos"])
        self.assertRaises(Exception, result)
