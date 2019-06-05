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
