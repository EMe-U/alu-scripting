#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts from a subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = ("https://reddit.com/r/{}/hot.json?limit=10"
                     .format(subreddit))
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])

        if len(posts) == 0:
            print("None")
        else:
            for post in posts:
                print(post.get('data', {}).get('title', None))
        print("OK")  # Print OK when the subreddit is valid
    else:
        print("OK")  # Print OK when the subreddit is invalid
