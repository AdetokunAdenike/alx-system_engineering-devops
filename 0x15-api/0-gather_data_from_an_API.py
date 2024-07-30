#!/bin/python3
"""
This script retrives and displays the TODO list progress of an employee
    gitven their employee ID using a REST API.
"""

import requests
import sys

def main():
    url = "https://jsonplaceholder.typicode.com/"

    if len(sys.argv) != 2:
        print("Usage: python <script> <employee_id>")
        sys.exit(1)
        
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_response = requests.get(url + "users/{}".format(employee_id))
    if user_response.status_code != 200:
        print("Employee not found")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    params = {"userId": employee_id}
    todos_response = requests.get(url + "todos", params=params)
    if todos_response.status_code != 200:
        print("Todos not found")
        sys.exit(1)

    todo = todos_response.json()

    completed = [todo.get("title") for todo in todos if todo.get("completed")]

    print("Employee {} is done with tasks({}/{}:)".format(employee.name, len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
