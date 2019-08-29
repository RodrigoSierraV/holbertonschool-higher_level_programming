#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""

from requests import get
from sys import argv

if __name__ == '__main__':

    if get(argv[1]).status_code >= 400:
        print('Error code: {}'.format(get(argv[1]).status_code))
    else:
        print(get(argv[1]).text)
