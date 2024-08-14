#!/usr/bin/python3
"""
This module defines the function `fetch_top_ten`.
"""

import requests
from sys import argv

def fetch_top_ten(subreddit):
    """
    Fetch and print the titles of the top 10 hot posts for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None: Prints the titles of the top 10 hot posts or None if the subreddit is invalid.
    """
    headers = {'User-Agent': 'MyUniqueAgent:v1.0 (by /u/yourusername)'}
    api_url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an error for bad status codes
        
        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:
            raise ValueError("Invalid subreddit or no posts found")
        
        for post in posts:
            title = post.get('data', {}).get('title')
            if title:
                print(title)
            else:
                print("Untitled Post")
    except (requests.RequestException, ValueError) as e:
        print(None)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: ./fetch_top_ten.py <subreddit>")
    else:
        fetch_top_ten(argv[1])
