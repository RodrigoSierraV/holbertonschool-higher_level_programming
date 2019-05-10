#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        new = [i if i != search else replace for i in my_list]
        return new
    return my_list
