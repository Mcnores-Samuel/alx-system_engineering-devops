#!/usr/bin/python3
"""Module to request top 10 hot posts in a subreddit"""
import requests


def top_ten(subreddit):
    """Function to request top 10 hot posts in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data").get("children")
    for post in results:
        print(post.get("data").get("title"))


if __name__ == "__main__":
    top_ten("programming")