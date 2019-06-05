#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a
       JSON representation

       Args:
            my_obj: string to serialize
            filename: file to save JSON representation of my_obj

       Return: Nothing"""

    import json

    with open(filename, mode='w', encoding='utf-8') as filename:
        json.dump(my_obj, filename)
