#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/?id={}'.format(user_id))
    user_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
            user_id))

    count = 0
    user_data = user_data.json()
    user_todos = user_todos.json()

    for todo in user_todos:
        if todo.get('completed'):
            count += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user_data[0].get('username'), count, len(user_todos)))
    for todo in user_todos:
        if todo.get('completed'):
            print("\t {}".format(todo.get('title')))
