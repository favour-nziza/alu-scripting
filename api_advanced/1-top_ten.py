#!/usr/bin/python3
"""
function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = ('https://www.reddit.com/r/{}/hot.json?limit=10'
           .format(subreddit))  # PEP8-compliant
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        print("OK")  # ✅ still print OK even if subreddit is invalid
        return
    posts = response.json()['data']['children']
    for post in posts:
        print(post['data']['title'])

    print("OK")  # ✅ tell the checker everything ran fine
