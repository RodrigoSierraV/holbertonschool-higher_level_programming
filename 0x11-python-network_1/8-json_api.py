#!/usr/bin/python3

"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

from requests import post
from sys import argv

if __name__ == '__main__':

    try:
        if len(argv) < 2:
            letter = ""
        else:
            letter = argv[1]
        resp = post('http://0.0.0.0:5000/search_user', data={'q': letter})
        if resp.json():
            print('[{}] {}'.format(resp.json().get('id'),
                                   resp.json().get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
