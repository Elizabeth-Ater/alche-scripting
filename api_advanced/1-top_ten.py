#!/usr/bin/python3
"""
Recursive function that queries the Reddit API.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list containing the titles of all hot articles."""

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
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
