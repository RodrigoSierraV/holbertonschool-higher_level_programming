#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "XCIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = ""
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = 65465
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
