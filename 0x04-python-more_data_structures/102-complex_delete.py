#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dlt = [i for i, y in a_dictionary.items() if y == value]
    for y in dlt:
        if y in a_dictionary:
            del a_dictionary[y]
    return a_dictionary
