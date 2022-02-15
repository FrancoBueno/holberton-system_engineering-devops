#!/usr/bin/python3
"""
    How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """ Subs of reddit """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by u/Frankitooo019)'
    }
    resp = requests.get(url, headers=header, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    else:
        resultado = resp.json().get('data')
        return resultado.get('subscribers')
