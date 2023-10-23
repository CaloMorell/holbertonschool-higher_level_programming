#!/usr/bin/python3
"""Test Module for testing the Base class"""


import unittest
from rectangle import Test_Rectangle
from square import Test_Square
from base import Test_Base


class TestBase(unittest.TestCase):
    """Class for the tests"""

    def test_base(self):
        """The tests"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        a = Base(89)
        self.assertEqual(a.id, 89)
