#!/usr/bin/python3
"""This module contains a function that queries the Reddit API and returns the
number of subscribers for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests as r


def number_of_subscribers(subreddit):
    """This function queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    response = r.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0