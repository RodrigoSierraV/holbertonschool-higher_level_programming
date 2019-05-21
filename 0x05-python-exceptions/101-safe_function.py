#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    div = None
    try:
        div = fct(*args)
        return div
    except (ZeroDivisionError, IndexError,
            ValueError, TypeError) as er:
        print("Exception: {}".format(er), file=stderr)
        return div
