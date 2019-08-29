#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import urllib.error
from sys import argv

if __name__ == '__main__':

    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode('utf8'))
    except urllib.error.HTTPError as err:
            print('Error code: {}'.format(err.code))
