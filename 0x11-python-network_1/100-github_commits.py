#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of a repository
"""

from requests import get
from sys import argv

if __name__ == '__main__':

    try:
        resp = get('https://api.github.com/repos/{}/{}/commits'.format(
                    argv[2], argv[1]))
        for commit in resp.json()[:10]:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit').get('author').get('name'))
    except:
        pass
