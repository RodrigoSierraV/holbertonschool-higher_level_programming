#!/usr/bin/python3
def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
       and returns the number of characters added

        Args:
             filename: file to append in
             text: string to append in filename
        Return:
               number of charaters added"""

    with open(filename, mode='a', encoding='utf-8') as written:
        return written.write(text)
