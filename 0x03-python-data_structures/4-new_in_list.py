#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        new = my_list[:]
        new[idx] = element
        return new
