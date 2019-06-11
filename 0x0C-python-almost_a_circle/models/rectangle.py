#!/usr/bin/python3
"""Module that defines a rectangle



"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor that defines instance attributes
           width, height, x and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """Definition of getters and setters for all attributes"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Method that computes the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Method that prints in stdout the Rectangle instance
           with the character #"""
        for j in range(self.__y):
            print('')
        for i in range(self.__height):
            print("{}".format(' ' * self.__x + '#' * self.__width))

    def __str__(self):
        """Informal representation of class Rectangle in a string"""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Method that assigns an argument to each attribute
           Args:
                *args: variable number of arguments"""
        if len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Method that returns the dictionary representation of a Rectangle"""
        return self.__dict__
