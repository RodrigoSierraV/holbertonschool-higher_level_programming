#!/usr/bin/python3
def inherits_from(obj, a_class):
    if not issubclass(type(obj), a_class) or type(obj) == a_class:
        return False
    return True
