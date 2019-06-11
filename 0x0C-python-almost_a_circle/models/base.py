#!/usr/bin/python3
"""Base class of the project. The goal of it is to manage id attribute
   in all your future classes and to avoid duplicating the same code.



"""
import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that defines public attribute id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """Method that returns the JSON string representation of 
           list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
