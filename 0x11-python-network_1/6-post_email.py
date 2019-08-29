#!/usr/bin/python3
"""script that takes in a URL, sends a request to the
URL and displays the value of the variable X-Request-Id
in the response header"""

from requests import post
from sys import argv

if __name__ == '__main__':

    try:
        email = {'email': argv[2]}
        resp = post(argv[1], data=email)
        print(resp.text)
    except:
        pass
