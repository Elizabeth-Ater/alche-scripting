#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:alche-scripting:v1.0 (by /u/ALU)"
    }

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        print("None")
        return

    posts = response.json().get("data", {}).get("children", [])

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
