#!/usr/bin/python3
"""Class that define the base for geometric shapes



"""


class BaseGeometry:

    def area(self):
        """Method not defined"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates a value if it's an integer
           Args:
                name: name of the object
                value: object to analize
           Raises: TypeError and ValueError"""

        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

"""Class that defines a rectangle and inherits from BaseGeometry



"""


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        """Defines attributes for rectangle"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns an string as informal representation of the instance"""
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height

"""Class that defines a Square and inherits from Rectangle



"""


class Square(Rectangle):

    def __init__(self, size):
        """Defines attributes for square"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Computes the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """Returns an string as informal representation of the instance"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
