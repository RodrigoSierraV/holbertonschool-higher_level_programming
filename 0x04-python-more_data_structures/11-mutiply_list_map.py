#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    def mul(m):
        return m * number
    return list(map(mul, my_list))
