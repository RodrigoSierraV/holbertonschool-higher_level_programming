#!/usr/bin/python3
def add_attribute(obj, name, value):
    """Function that adds a new attribute to obj

       Args:
            obj: instance of another class
            name: name of the new attribute
            value: value of the new attribute"""

    if name not in dir(obj) and '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
