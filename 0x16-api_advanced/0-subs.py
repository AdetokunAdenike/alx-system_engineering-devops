#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Base URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom headers to avoid Too Many Requests error
    headers = {
        'User-Agent': 'Python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)'
    }
    
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # If the status code is 200, parse the JSON response
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        
        # If the status code indicates a not found or similar, return 0
        return 0
        
    except requests.RequestException as e:
        # If there's an error in the request, return 0
        print(f"An error occurred: {e}")
        return 0
