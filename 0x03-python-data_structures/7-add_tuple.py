#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    w = x = y = z = 0
    if len(tuple_a) == 1:
        w = tuple_a[0]
    elif len(tuple_a) >= 2:
        w = tuple_a[0]
        x = tuple_a[1]
    if len(tuple_b) == 1:
        y = tuple_b[0]
    elif len(tuple_b) >= 2:
        y = tuple_b[0]
        z = tuple_b[1]
    new = tuple((w + y, x + z))
    return new
