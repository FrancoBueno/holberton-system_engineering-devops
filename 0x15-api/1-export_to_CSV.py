#!/usr/bin/python3
""" API Project """

import requests
from sys import argv
import csv


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

    with open ("{}.csv".format(argument), mode='w') as File:
        writer = csv.writer(File)
        for tasks in task:
            writer.writerow([name.get("id"), name.get("username"), tasks.get("completed"), tasks.get("title")])

