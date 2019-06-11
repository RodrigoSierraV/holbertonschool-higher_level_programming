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

    def __str__(self):
        """Informal representation of a square with a string"""
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x,
                                                 self.y, self.width)

    """Defining getter and setter for size"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute
           Args:
                *args: variable number of arguments"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) == 4:
            self.y = args[3]

        if len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
