#!/usr/bin/python3
def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

       Args:
            my_obj: string to serialize

       Return: JSON representation of my_obj"""

    import json

    return json.dumps(my_obj)
