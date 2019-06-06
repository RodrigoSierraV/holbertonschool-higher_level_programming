#!/usr/bin/python3
"""Class Student that defines a student by name and age



"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Define attributes first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        if attrs is not None and False not in [
                isinstance(i, str) for i in attrs]:
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json and len(json) > 0:
            new = json.keys()
            new = [i for i in new if i in self.__dict__.keys()]
            for i in new:
                self.__dict__[i] = json[i]
