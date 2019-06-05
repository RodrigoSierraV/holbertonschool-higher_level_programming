#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file(UTF8) and prints it to stdout

        Args:
             filename: file to ope and count lines. Can be an empty string
             nb_lines: number of lines to read. Read the entire file if
                       nb_lines is lower or equal to 0 OR greater or equal
                       to the total number of lines of the file.
        Return:
               Nothing"""
    count = 0

    with open(filename, mode='r', encoding='utf-8') as reading:
        for lines in reading:
            count += 1

    with open(filename, mode='r', encoding='utf-8') as reading:
        if nb_lines <= 0 or nb_lines >= count:
            print(reading.read(), end='')
        for i in range(nb_lines):
            print(reading.readline(), end='')
