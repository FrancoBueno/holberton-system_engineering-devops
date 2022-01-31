#!/usr/bin/python3
""" API Project """

import requests
from sys import argv

if __name__ == "__main__":
    argument = argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + argument).json()
    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argument).json()
    taskscompleted = []
    for tasks in task:
        if tasks.get("completed") is True:
            taskscompleted.append(tasks.get('title'))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            name.get('name'), len(taskscompleted), len(task)))
    print('\n'.join('\t {}'.format(task) for task in taskscompleted))
