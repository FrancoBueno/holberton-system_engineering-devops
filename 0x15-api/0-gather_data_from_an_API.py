#!/usr/bin/python3
""" API Project """


if __name__ == "__main__":
    import requests
    from sys import argv

    Ids = argv[1]
    users = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(Ids), verify=False).json()
    tass = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                       format(Ids), verify=False).json()
    taskscompleted = []
    for tasks in tass:
        if tasks.get('completed') is True:
            taskscompleted.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(users.get('name'), len(taskscompleted), len(tass)))
    print("\n".join("\t {}".format(tasks) for tasks in taskscompleted))
