#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Fetch and print the titles of the first 10 hot posts from a subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    # Request with no redirects
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        # Parse JSON response
        json_data = response.json().get("data", {})
        children = json_data.get("children", [])
        
        # Print the title of each post
        for post in children:
            print(post.get("data", {}).get("title", ""))
    else:
        print(None)
