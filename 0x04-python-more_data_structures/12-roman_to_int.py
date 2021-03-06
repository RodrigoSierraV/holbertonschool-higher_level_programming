#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        number = i = 0
        rm = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < len(roman_string) - 1:
            trn = rm[roman_string[i]]
            if rm[roman_string[i + 1]] > rm[roman_string[i]]:
                trn = -rm[roman_string[i]]
            number += trn
            i += 1
        return number + rm[roman_string[i]]
    else:
        return 0
