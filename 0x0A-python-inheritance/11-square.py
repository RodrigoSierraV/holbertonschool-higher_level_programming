#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)

    def area(self):
        return self.__width * self.__height

class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
