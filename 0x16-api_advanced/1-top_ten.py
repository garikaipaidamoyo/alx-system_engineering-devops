#!/usr/bin/python3
"""
1-top_ten.py
"""


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    import requests
    hot_posts = requests.get(
            "https://www.reddit.com/r/{}/hot.json?limit=10"
            .format(subreddit),
            headers={"User-Agent": "Custom"},
            allow_redirects=False
            )
    if hot_posts.status_code >= 300:
        print("None")
    else:
        for posts in hot_posts.json().get("data").get("children"):
            print(posts.get("data").get("title"))
