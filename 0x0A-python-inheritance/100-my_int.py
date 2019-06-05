#!/usr/bin/python3
"""Class that inherits from class int



"""


class MyInt(int):

    def __eq__(self, other):
        """Method that checks for equivalences with other objects
           Args:
                other: object to compare
           Return: Method __ne__ of the class int"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Method that checks for differences with other objects
           Args:
                other: object to compare
           Return: Method __eq__ of the class int"""

        return super().__eq__(other)
