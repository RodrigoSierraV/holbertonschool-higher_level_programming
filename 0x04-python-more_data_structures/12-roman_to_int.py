#!/usr/bin/python3
def roman_to_int(roman_string):
    number = i = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    while i < len(roman_string) - 1:
        if roman[roman_string[i + 1]] > roman[roman_string[i]]:
                roman[roman_string[i]] = -roman[roman_string[i]]
        number += roman[roman_string[i]]
        i += 1
    return number + roman[roman_string[i]]
