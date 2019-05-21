#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        sys.stderr.write("Exception: Wrong Type\n")
        return False
    except ValueError:
        sys.stderr.write("Exception: Wrong Type\n")
        return False
