#!/usr/bin/python3
""" API Project """


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv
    argument = argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/".json()
    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos/".json()
    user = {}
    for usr in name:
        if usr["id"] == int(argv[1]):
            user = dict(usr)
            break
    taskcompleted = []
    user_all = []
    user_comp = []

    for usr in task:
        if usr["userId"] == int(argv[1]):
            user_all.append(dict(usr))
            if usr["completed"] is True:
                taskcompleted =  taskcompleted + 1
                user_comp.append(dict(usr))

    print("Employee {} is done with tasks({}/{}):"
          .format(user["name"], taskcompleted, len(user_all)))

    for tasks in user_comp:
        print("\t {}".format(tasks["title"]))
