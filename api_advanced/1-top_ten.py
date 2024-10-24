#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts from a subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children")
        
        if not children:
            print(None)
        else:
            for post in children:
                print(post.get("data").get("title"))
    else:
        print(None)
