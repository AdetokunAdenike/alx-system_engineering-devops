#!/usr/bin/python3
"""Fetches and exports to-do tasks for all employees to a JSON file."""
import json
import requests

def fetch_all_tasks():
    """
    Fetches to-do tasks for all employees and formats them into a dictionary.
    
    Returns:
        dict: A dictionary where keys are user IDs and values are lists of
              dictionaries containing task details, completion status, and username.
    """
    base_url = "https://jsonplaceholder.typicode.com/"
    employees = requests.get(f"{base_url}users").json()
    
    tasks_by_user = {}
    for employee in employees:
        user_id = employee["id"]
        todos_url = f"{base_url}todos"
        todos = requests.get(todos_url, params={"userId": user_id}).json()
        
        tasks_by_user[user_id] = [
            {
                "username": employee["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            } for todo in todos
        ]
    
    return tasks_by_user

if __name__ == "__main__":
    tasks_data = fetch_all_tasks()
    
    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks_data, file, indent=4)
