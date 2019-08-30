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
            for movie in names.get('films'):
                resp2 = get(movie)
                print('\t{}'.format(resp2.json().get('title')))
        nextp = resp.json().get('next')
        while nextp:
            resp1 = get(nextp)
            for page in resp1.json().get('results'):
                print(page.get('name'))
                for movie in page.get('films'):
                    resp2 = get(movie)
                    print('\t{}'.format(resp2.json().get('title')))
            nextp = resp1.json().get('next')
    except:
        pass
