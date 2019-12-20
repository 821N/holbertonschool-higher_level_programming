#!/usr/bin/python3
"""
    11. Student to JSON
"""


class Student:
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to dict """
        if type(attrs) == list:
            l = {}
            for name in attrs:
                l[name] = getattr(self, name)
            return l
        else:
            return self.__dict__
