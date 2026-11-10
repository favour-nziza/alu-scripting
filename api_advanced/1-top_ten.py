#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/favour-nziza)"}
    response = requests.get(url,
                            headers=headers,
                            params={"limit": 10},
                            allow_redirects=False)
    print("DBG", subreddit, type(response), response.status_code,
          repr(response.text[:60]))
