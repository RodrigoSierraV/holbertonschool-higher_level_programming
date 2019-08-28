#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the
response.
"""

import urllib.request
from sys import argv

try:

    with urllib.request.urlopen(argv[1]) as resp:
        print(resp.getheader('X-Request-Id'))
except:
    pass
