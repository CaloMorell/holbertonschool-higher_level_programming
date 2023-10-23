#!/usr/bin/python3
"""The first class Base"""


class Base:
"""Represent base model"""


    __nb_objects = 0
    """private class attribute"""


    def __int__(self, id=None)
    """class constructor"""
    if id is not None:
        self.id = id
    else:
        Base.__nb_object += 1
        self.id = Base.__nb_object
