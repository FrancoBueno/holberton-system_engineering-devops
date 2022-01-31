#!/usr/bin/python3
""" API Project """

import requests
import csv
import json


if __name__ == "__main__":
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/").json()

    for users in name:
        task = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId=" + str(users.get("id"))).json()
    with open ("todo_all_employees.json", mode='w') as File:
        dictoftasks = [{"username": users.get("username"), "task": tasks.get("title"), "completed": tasks.get("completed")} for tasks in task]
        dictnew = {}
        dictnew.update({users.get("id"): dictoftasks})
        json.dump(dictnew, File)
    
