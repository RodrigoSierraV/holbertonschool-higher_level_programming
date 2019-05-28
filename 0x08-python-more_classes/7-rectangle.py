#!/usr/bin/python3
"""Class that defines a rectangle

"""


class Rectangle:
    """Args:
            width: integer
            height: integer
    """

    """Integer that stores the number of instances of the class"""
    number_of_instances = 0

    """symbol for string representation of the rectangle"""
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle or 0"""
        if self.__height is 0 or self.__width is 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        """Creates the a string with the representation of the rectangle"""
        string = ""
        if self.__width is not 0 or self.__height is not 0:
            for i in range(self.__height):
                for y in range(self.__width):
                    string += ''.join(str(self.print_symbol))
                if i < self.__height - 1:
                    string += '\n'
        else:
            string += '\n'
        return string

    def __repr__(self):
        """official string representation of the retangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """Destructor of the object rectangle"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
