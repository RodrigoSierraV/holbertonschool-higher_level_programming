#!/usr/bin/python3
"""
script that takes in a string and sends a search request
to the Star Wars API
"""

from requests import get
from sys import argv

if __name__ == '__main__':

    try:
        resp = get('https://swapi.co/api/people/',
                   params={'search': argv[1]})
        print('Number of results: {}'.format(resp.json().get('count')))
        for names in resp.json().get('results'):
            print(names.get('name'))
    except:
        pass
