#!/usr/bin/python3
"""
This script retrieves and displays the TODO list progress of
    an employee given their employee ID using a REST API.
Returns to-do list information for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    # The Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Using the provided employee ID, get the employee information
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Using the provided employee's ID, get the to-do list for the employee
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter and count completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name with corresponding number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Print the completed tasks one after the other with indentation
    [print("\t {}".format(complete)) for complete in completed]
