#!/usr/bin/python3
def number_of_lines(filename=""):
    """ function that returns the number of lines of a text file

        Args:
             filename: file to ope and count lines. Can be an empty string
        Return:
               Integer with the count of the lines"""
    count = 0

    with open(filename, mode='r', encoding='utf-8') as reading:
        for lines in reading:
            count += 1
    return count
