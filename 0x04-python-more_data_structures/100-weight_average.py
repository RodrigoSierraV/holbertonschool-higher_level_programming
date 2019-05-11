#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    mul = 1
    summ = sum1 = 0
    for i in my_list:
        mul = 1
        for y in i:
            mul = mul * y
        summ = summ + mul
        sum1 = sum1 + i[1]
    return summ / sum1
