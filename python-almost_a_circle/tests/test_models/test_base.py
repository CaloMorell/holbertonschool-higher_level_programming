#!/usr/bin/python3
"""Test Module for testing the Base class"""


import unittest
from test_rectangle import Rectangle
from test_square import Square
from test_base import Base
import test_rectangle
import test_square
import test_base


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
