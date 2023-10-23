#!/usr/bin/python3
"""The first class Base"""
import json
from os import path


class Base:


    __nb_objects = 0


    def __int__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
        self.id = Base.__nb_objects



    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)



    @classmethod
    def save_to_file(cls, list_objs):

        flname = cls.__name__ + '.json'
        dic = []
        if list_objs is not None:
            dic = [a.to_dictionary() for a in list_objs]
        with open(flname, 'w') as f:
            f.write(cls.to_json_string(dic))


    @staticmethod
    def from_json_string(json_string):

        if json_string is None or not json_string:
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):

        if cls.__name__ == 'Square':
            new_base = cls(1)
        else:
            new_base = cls(1, 1)
        cls.update(new_base, **dictionary)
        return new_base


    @classmethod
    def load_from_file(cls):

        flname = cls.__name__ + '.json'
        if path.isfile(flname):
            with open(flname, 'r') as f:
                my_l = cls.from_json_string(f.read())
            return [cls.create(**a) for a in my_l]
        return []
