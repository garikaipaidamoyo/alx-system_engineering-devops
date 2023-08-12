#!/usr/bin/python3
"""
2-recurse.py
"""


def recurse(subreddit, hot_list=[], after=""):
    """
    function that queries the Reddit
    API and returns a list containing
    the titles of all hot articles for
    a given subreddit.
    """
    import requests
    hot_articles = requests.get(
            "https://www.reddit.com/r/{}/.json"
            .format(subreddit),
            headers={"User-Agent": "Custom"},
            params={"after": after},
            allow_redirects=False
            )
    if hot_articles.status_code >= 400:
        return None

    hot_arts = hot_list + [articles.get("data").get("title")
            for articles in hot_articles.json()
            .get("data")
            .get("children")]

    article = hot_articles.json()
    if not article.get("data").get("after"):
        return hot_arts

    return recurse(subreddit, hot_arts, article.get("data").get("after"))
