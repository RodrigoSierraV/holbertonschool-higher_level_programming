#!/usr/bin/python3
"""Base class of the project. The goal of it is to manage id attribute
   in all your future classes and to avoid duplicating the same code.



"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that defines public attribute id""" 
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
