#!/usr/bin/python3
"""Exports data in the JSON format."""
import json
import requests

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    obj = {}
    for user in users:
        value_list = []
        for todo in todos:
            if todo.get('userId') == user.get('id'):
                dict_d = {}
                dict_d["task"] = todo.get('title')
                dict_d["completed"] = todo.get('completed')
                dict_d["username"] = user.get('username')
                value_list.append(dict_d)
        obj["{}".format(user.get('id'))] = value_list
    with open('todo_all_employees.json', 'w') as file:
        json.dump(obj, file)
