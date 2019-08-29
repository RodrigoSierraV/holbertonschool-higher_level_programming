#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import urllib.request
import urllib.parse
from sys import argv

try:
    email = urllib.parse.urlencode({'email': argv[2]}).encode()
    with urllib.request.urlopen(argv[1], data=email) as resp:
        print(resp.read().decode('utf-8'))
except:
    pass
