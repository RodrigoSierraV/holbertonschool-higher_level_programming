#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Args:
            list_of_integers: list of unordered integers"""

    peaks = None
    uniq = []
    for i in range(len(list_of_integers)):
        if list_of_integers[i - 1] < list_of_integers[i] and\
           list_of_integers[i + 1] < list_of_integers[i]:
            peaks = list_of_integers[i]
        if list_of_integers[i] not in uniq:
            uniq.append(list_of_integers[i])

    if len(uniq) == 1:
        return uniq[0]

    return peaks
