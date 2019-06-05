#!/usr/bin/python3
def load_from_json_file(filename):
    """function that creates an Object from a JSON file

       Args:
            filename: JSON file to read

       Return: Python object"""

    import json

    with open(filename, mode='r', encoding='utf-8') as deser:
        return json.load(deser)
