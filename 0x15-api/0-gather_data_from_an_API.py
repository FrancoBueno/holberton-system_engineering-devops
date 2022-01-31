#!/usr/bin/python3
""" API Project """

import requests
from sys import argv

if __name__ == "__main__":
    def user():
        """ find the user"""
        req = requests.get('https://jsonplaceholder.typicode.com/users')
        lista = req.json()

        for usr in lista:
            if usr["id"] == int(argv[1]):
                return usr

    def todo():
        """ sadasdas """
        todo = []
        total = 0
        req = requests.get('https://jsonplaceholder.typicode.com/todos')
        lista = req.json()

        for todos in lista:
            if todos['userId'] == int(argv[1]):
                total += 1
            if todos['userId'] == int(argv[1]) and todos['completed'] is True:
                todo.append(todos["title"])
        return todo, total

    def user_todo():
        """ asdasdasd """
        i = 0

        userr = user()
        tode = todo()
        i = len(tode[0])

        print('Employee {} is done with tasks({}/{}):'.
              format(userr["name"], i, tode[1]))

        for x in range(i):
            print('\t {}'.format(tode[0][x]))

    user_todo()
