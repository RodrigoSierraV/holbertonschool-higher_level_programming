#!/usr/bin/python3
"""Module that defines a square and its attributes and methods



"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that describes a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of a square with instance attributes size, x, y
           and id"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Informal representation of a square with a string"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
            self.y, self.height)
