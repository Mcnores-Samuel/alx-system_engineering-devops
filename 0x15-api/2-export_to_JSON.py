#!/usr/bin/python3
"""exports response data to a json file"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get('username')

    obj = {}
    value_list = []
    for todo in todos:
        dict_d = {}
        dict_d["task"] = todo.get('title')
        dict_d["completed"] = todo.get('completed')
        dict_d["username"] = username
        value_list.append(dict_d)
    obj["{}".format(user.get('id'))] = value_list
    with open("{}.json".format(user.get('id')), 'w') as file:
        json.dump(obj, file)
