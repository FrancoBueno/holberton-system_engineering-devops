#!/usr/bin/python3
""" API Project """

import requests
from sys import argv
import json


if __name__ == "__main__":
    argument = argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argument)).json()
    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argument)).json()
    taskscompleted = [
        tasks.get("title") for tasks in task if tasks.get("completed")]

    with open("{}.json".format(argument), mode='w') as File:
        dictoftasks = [{'task': tasks.get("title"),
                        'completed': tasks.get("completed"),
                        "username": name.get("username")} for tasks in task]
        json.dump({task[0].get('userId'): dictoftasks}, File)
