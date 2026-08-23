#!/usr/bin/python3
"""
Recursively queries Reddit and counts keywords in hot article titles.
"""

import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """Count keywords in all hot article titles."""
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after:
        url += "?after={}".format(after)

    headers = {
        "User-Agent": "ALU-Reddit-API"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "")
        hot_list.append(title)

    after = data.get("after")

    if after is not None:
        return count_words(subreddit, word_list, hot_list, after)

    counts = {}

    for word in word_list:
        word = word.lower()
        if word not in counts:
            counts[word] = 0

    for title in hot_list:
        words = title.lower().split()

        for word in words:
            if word in counts:
                counts[word] += 1

    results = []

    for word, count in counts.items():
        if count > 0:
            results.append((word, count))

    results.sort(key=lambda x: (-x[1], x[0]))

    for word, count in results:
        print("{}: {}".format(word, count))
