#!/usr/bin/python3
""" API Project """

import csv
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    all = requests.get(url + "todos").json()
    user_dict = {}
    name_dict = {}
    for field in user:
        user_id = field.get("id")
        user_dict[user_id] = []
        name_dict[user_id] = field.get("username")

    for task in all:
        user_id = task.get("userId")
        task_dic = {}
        task_dic["task"] = task.get("title")
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = name_dict.get(user_id)
        user_dict.get(user_id).append(task_dic)

    with open("todo_all_employees" + ".json", "w") as jsonFile:
        json.dump(user_dict, jsonFile)
