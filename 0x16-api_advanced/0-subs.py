#!/usr/bin/python3
"""Module for task 0"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers to the subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Check if the request was successful
    except requests.RequestException:
        return 0

    data = response.json().get("data")
    if data:
        return data.get("subscribers", 0)
    return 0

# Example usage
print(number_of_subscribers("learnpython"))
