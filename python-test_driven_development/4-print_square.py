#!/usr/bin/python3
"""This module contains a function that
    prints a n sizesquare with the character #"""


def print_square(size):
    """prints a square with the character #.

    Arguments:
        size (int) -- size of the square.

    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(0, size):
        for c in range(0, size):
            if c != (size - 1):
                print("#", end="")
            else:
                print("#")
