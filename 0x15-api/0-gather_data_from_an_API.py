#!/usr/bin/python3
""" API Project """

import requests as req
from sys import argv
import json


if __name__ == "__main__":
    resp = req.get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    dic = json.loads(resp.text)
    name = dic.get('name')
    resp = req.get('https://jsonplaceholder.typicode.com/todos/?userId={}'.format(argv[1]))
    todo = json.loads(resp.text)
    tasks = len(todo)
    completed = [task for task in todo if task.get("completed")]
    k = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(name, k, tasks))

    for task in completed:
        print("\t", task.get("title"))
