#!/usr/bin/python3
"""Create a csv file from the response data via requests"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = user.get('username')

    with open('{}.csv'.format(user.get('id')), 'w') as file:
        for todo in todos:
            file.write('"{}","{}","{}",{}\n'.format(todo.get('userId'),
                                                    username,
                                                    todo.get('completed'),
                                                    todo.get('title')))
