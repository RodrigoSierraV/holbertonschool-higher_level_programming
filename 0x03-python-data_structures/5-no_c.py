#!/usr/bin/env python3
def no_c(my_string):
    if my_string:
        return my_string.translate({ord(i): None for i in "cC"})
    else:
        return my_string
