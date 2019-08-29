#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
import urllib.error
from sys import argv

try:
    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.read().decode('utf-8'))
except urllib.error.HTTPError as err:
    print('Error code: {}'.format(err.code))
