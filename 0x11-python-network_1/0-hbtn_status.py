#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
    print('Body response:')
    response = resp.read()
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
    print('\t- utf8 content: {}'.format(response.decode('utf-8')))
