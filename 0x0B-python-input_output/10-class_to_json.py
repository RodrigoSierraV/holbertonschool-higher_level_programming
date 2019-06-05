#!/usr/bin/python3
def class_to_json(obj):
    """ function that returns the dictionary description with simple
        data structure (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

    Args:
         obj: instance of a Class

    Return: a dictionary"""

    return str(repr(obj))
