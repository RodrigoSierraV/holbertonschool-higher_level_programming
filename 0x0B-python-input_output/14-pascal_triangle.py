#!/usr/bin/python3
def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascals
        triangle of n

        Args:
             n: times to compute Pascal's triangle
        Return: List of lists"""
    new = []
    if n <= 0:
        return new
    new = [1]
    for i in range(n - 1):
        if i is 0:
            add = new[:1] + new[-1:]
            new = [new]
        else:
            add = add[:1] + [sum(add[b:(b+2)]) for b in range((len(add) - 1))]\
                    + add[-1:]
        new.append(add)
    return new
