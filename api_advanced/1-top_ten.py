#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    If not a valid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:top.ten.checker:v1.0 (by /u/check)"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not results:
        print(None)
        return

    for post in results:
        print(post.get("data", {}).get("title"))
