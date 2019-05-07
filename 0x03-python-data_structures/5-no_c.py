#!/usr/bin/env python3
def no_c(my_string):
    return new = my_string.translate({ord(i): None for i in "cC"})
