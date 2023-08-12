#!/usr/bin/python3

def number_of_subscribers(subreddit):
    import requests
    sub_number = requests.get("https://www.reddit.com/r/{}/about.json"
                             .format(subreddit),
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if sub_number.status_code >= 300:
        return 0
    return sub_number.json().get("data").get("subscribers")
