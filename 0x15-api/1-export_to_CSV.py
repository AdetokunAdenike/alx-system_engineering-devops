#!/usr/bin/python3
"""Using what was done in the task #0, extend your Python script
to export data in the CSV format.."""

import csv
import requests
import sys


if __name__ == "__main__":
    # Retrieve the user ID from the command-line arguments passed to the script.
    user_id = sys.argv[1]

    # Specify the base URL for the JSON API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieve the  user information from the API and
    #   convert the response to a JSON object
    user = requests.get(url + "users/{}".format(user_id)).json()

    # Extract username from  user data
    username = user.get("username")

    # Retrieve the to-do list items for the specified user ID
    # and convert the response to a JSON object.
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Use list comprehension to iterate through the to-do list items and
    # write each item's details (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
