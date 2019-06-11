#!/usr/bin/python3
"""Base class of the project. The goal of it is to manage id attribute
   in all your future classes and to avoid duplicating the same code.



"""
import json
import os


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
           list_dictionaries
           Args:
                list_dictionaries: list of dictionaries
           Return: JSON string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def to_json_string(my_obj):
        """function that returns the JSON representation of an object (string)
           Args:
                my_obj: string to serialize
           Return: JSON representation of my_obj"""

        return json.dumps(my_obj)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method  that writes the JSON string representation of
           list_objs to a file.
           Args:
                list_objs: is a list of instances who inherits of Base
           Return: Nothing"""
        filename = cls.__name__ + '.json'
        if list_objs is None:
            with open(filename, mode='w', encoding='utf-8') as filew:
                return filew.write('[]')
        dicts = []
        for obj in list_objs:
            dicts.append(cls.to_dictionary(obj))
        text = cls.to_json_string(dicts)
        with open(filename, mode='w', encoding='utf-8') as filew:
            filew.write(text)

    @staticmethod
    def from_json_string(json_string):
        """Static Method that returns the list of the JSON string
           representation json_string.
           Args:
               json_string: is a string representing a list of dictionaries
           Return: list represented by json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with all attributes
           already set.
           Args:
                **dictionary: reference to a dictionary with attributes
           Return: an instance with all attributes from dictionary"""
        dummy = cls(3, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        filename = cls.__name__ + '.json'
        if not os.path.isfile(filename):
            return []
        string = ''
        with open(filename, mode='r', encoding='utf-8') as read_instances:
            string += read_instances.read()
        dict_instances = cls.from_json_string(string)
        list_instances = []
        for objs in dict_instances:
            list_instances.append(cls.create(**objs))
        return list_instances
