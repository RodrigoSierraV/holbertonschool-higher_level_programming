#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        string = ""
        if self.__size is not 0:
            b = y = 0
            for t in range(self.__position[1]):
                string += "\n"
            for i in range(self.__size):
                b = y = 0
                while y < self.__size:
                    if b < self.__position[0]:
                        string += " "
                        b += 1
                        continue
                    string += "#"
                    y += 1
                if i < self.__size - 1:
                    string += "\n"
        return string

    def my_print(self):
        if self.__size is not 0:
            b = y = 0
            for t in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                b = y = 0
                while y < self.__size:
                    if b < self.__position[0]:
                        print(" ", end="")
                        b += 1
                        continue
                    print("#", end="")
                    y += 1
                print("")
        else:
            print("")
