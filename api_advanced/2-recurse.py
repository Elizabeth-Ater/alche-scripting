#!/usr/bin/python3
"""
Recursively queries the Reddit API and returns all hot post titles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list containing the titles of all hot articles."""
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
        title = post.get("data", {}).get("title")
        hot_list.append(title)

    after = data.get("after")

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
