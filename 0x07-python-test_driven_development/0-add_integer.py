#!/usr/bin/python3
"""This module adds 2 integers.
     Args:
          a: integer or float
          b: integer or float
"""


def add_integer(a, b=98):
    """Raises:
          TypeError: if a or b aren't integer or float
       Return: an integer with the result of the sum"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
