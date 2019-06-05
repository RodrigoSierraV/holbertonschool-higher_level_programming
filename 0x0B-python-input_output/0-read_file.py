#!/usr/bin/python3
def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout

        Args:
             filename: name of the file to read. Can be empty string

        Return: Nothing"""

    with open(filename, mode='r', encoding='utf-8') as reading:
        print(reading.read(), end='')
