#!/usr/bin/python3
""" 3-count.py """
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """ prints a sorted count of given keywords """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/favour-nziza)"}
    response = requests.get(url,
                            headers=headers,
                            params={"after": after, "limit": 100},
                            allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in counts:
                counts[word] += 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    weights = {}
    for word in word_list:
        weights[word.lower()] = weights.get(word.lower(), 0) + 1

    totals = [(word, count * weights.get(word, 1))
              for word, count in counts.items()]
    for word, total in sorted(totals, key=lambda kv: (-kv[1], kv[0])):
        if total > 0:
            print("{}: {}".format(word, total))
