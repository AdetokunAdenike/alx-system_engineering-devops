#!/usr/bin/python3
"""
Exports to-do list data for all employees in JSON format.

Fetches user and to-do list information from JSONPlaceholder API
and writes it to 'todo_all_employees.json'. Each entry includes
task details, completion status, and the associated username.
"""

import json
import requests

def fetch_user_data():
"""
Retrieve user details and their to-do lists for all employees.

Returns:
    dict: Dictionary where keys are user IDs and values are lists
              of tasks with details, completion status, and username.
"""
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users (employees)
    users = requests.get(f"{base_url}users").json()

    # Dictionary for all to-do lists
    data_to_export = {}
    for user in users:
        user_id = user["id"]
        user_url = f"{base_url}todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    data_to_export = fetch_user_data()

    # Write data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
