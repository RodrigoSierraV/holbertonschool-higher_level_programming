#!/usr/bin/python3
"""function that prints a square with the character #.
   Args:
        size: integer greater than zero

"""


def print_square(size):
    """Raises: TypeError if size isn't integer or is a float less than zero
               ValueError if size is less than zero
       Return: Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size is not 0:
        for i in range(size):
            for y in range(size):
                print("#", end="")
            print("")
