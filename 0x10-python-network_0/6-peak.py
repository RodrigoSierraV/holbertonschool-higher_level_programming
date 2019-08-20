#!/usr/bin/python3

def find_peak(list_of_integers):

    peaks = None
    uniq = []
    for i in range(len(list_of_integers) - 1):
        if list_of_integers[i - 1] < list_of_integers[i] and\
        list_of_integers[i + 1] < list_of_integers[i]:
            peaks = list_of_integers[i]
        if list_of_integers[i] not in uniq:
            uniq.append(list_of_integers[i])

    if len(uniq) == 1:
        return uniq[0]

    return peaks
