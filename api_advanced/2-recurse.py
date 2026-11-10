#!/usr/bin/python3
""" 2-recurse.py """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """ returns list with titles of all hot articles in a subreddit """
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/favour-nziza)"}
    params = {"after": after, "limit": 100}
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    hot_list += [post.get("data", {}).get("title")
                 for post in data.get("children", [])]
    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
