#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = [my_list[i] for i in range(len(my_list))
           if my_list[i] not in my_list[(i + 1):]]
    return sum(add)
