#!/usr/bin/python3
""" API Project """


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv
    argument = argv[1]
    name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            argument)).json()
    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            argument)).json()
    taskscompleted = [
        tasks.get("title") for tasks in task if tasks.get("completed")]

    with open("{}.csv".format(argument), mode='w') as File:
        writer = csv.writer(File, quoting=csv.QUOTE_ALL)
        for tasks in task:
            writer.writerow([name.get("id"), name.get("username"),
                            tasks.get("completed"), tasks.get("title")])
