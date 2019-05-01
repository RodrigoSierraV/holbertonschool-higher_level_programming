#!/usr/bin/python3
def remove_char_at(str, n):
    copy = str[:]
    if n >= 0:
        copy = copy[:n] + copy[(n + 1):]
    return copy
