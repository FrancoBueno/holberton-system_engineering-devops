#!/usr/bin/python3
"""
    How many top_ten?
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ top_ten bro """
    if subreddit is None or type(subreddit) is not str:
        return None
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by u/Frankitooo019)'
    }
    params = {'limit': '100',
              'count': count,
              'after': after
    }
    resp = requests.get(
           url, headers=header, params=params, allow_redirects=False)
    if resp.status_code == 404:
        return None
    else:
        resultado = resp.json().get("data")
        after = resultado.get('after')
        count += resultado.get('dist')
        for c in resultado.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
