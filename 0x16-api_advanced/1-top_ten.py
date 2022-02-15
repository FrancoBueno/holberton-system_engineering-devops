#!/usr/bin/python3
"""
    How many top_ten?
"""
import requests


def top_ten(subreddit):
    """ top_ten bro """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by u/Frankitooo019)'
    }
    parameters = {'limits' : '10'}
    resp = requests.get(url, headers=header, params=parameters, allow_redirects=False)
    if resp.status_code == 404:
        return None
    else:
        resultado = resp.json().get('data')
        [print (r.get('data').get('title')) for r in resultado.get('children')]
