#!/usr/bin/python3
"""
This module contains the function `top_ten` to fetch the top 10 posts from a subreddit.
"""

import requests
from sys import argv

def top_ten(subreddit):
    """
    Fetch and print the titles of the top 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles or 'None' if the subreddit is invalid.
    """
    headers = {'User-Agent': 'Python:subreddit.top_ten:v1.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for successful request
        if response.status_code != 200:
            print(None)
            return
        
        # Parse the JSON response
        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:
            print(None)
            return
        
        # Print titles of the top 10 posts
        for post in posts:
            print(post.get('data', {}).get('title', 'Untitled Post'))

    except requests.RequestException as e:
        # Handle any request errors
        print(None)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: ./1-top_ten.py <subreddit>")
    else:
        top_ten(argv[1])
