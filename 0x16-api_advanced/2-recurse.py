#!/usr/bin/python3
"""
Contains recurse function to fetch all hot post titles recursively
from a given subreddit using the Reddit API.
"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively fetches titles of all hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List of hot post titles (used internally).
        after (str): The ID of the last post fetched (for pagination).
        count (int): The number of posts fetched so far.

    Returns:
        list: A list containing titles of all hot posts, or None if subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raises HTTPError for bad requests (e.g., 404)
    except requests.RequestException:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += results.get("dist", 0)
    for c in results.get("children", []):
        hot_list.append(c.get("data", {}).get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
