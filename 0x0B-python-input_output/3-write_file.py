#!/usr/bin/python3
def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and returns
       the number of characters written

        Args:
             filename: file to write in
             text: string to write in filename
        Return:
               number of charaters written"""

    with open(filename, mode='w', encoding='utf-8') as written:
        return written.write(text)
