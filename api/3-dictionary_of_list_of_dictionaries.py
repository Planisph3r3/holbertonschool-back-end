#!/usr/bin/python3
"""Using a mock api for fetch information"""
import json
import requests
from sys import argv, exit


def main():
    """Requesting the name and the todos of an enployee"""

    all_employees = {}

    for id in range(1, 11):
        url_id = f"https://jsonplaceholder.typicode.com/users/{id}"
        url_todos = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

        response = requests.get(url_id)

        if response.status_code != 200:
            print(f"Cannot fetch data")
            exit()

        data = response.json()
        EMPLOYEE_NAME = data['username']

        response = requests.get(url_todos)

        if response.status_code != 200:
            print(f"Cannot fetch data")
            exit()

        todos = response.json()
        list_todos = []
        dict_todos = {}

        all_tasks = [todo['title'] for todo in todos]
        status_task = [todo['completed'] for todo in todos]

        for index in range(0, len(all_tasks)):
            dict_todos = {
                'username': EMPLOYEE_NAME,
                'task': all_tasks[index],
                'completed': status_task[index]
            }

            list_todos.append(dict_todos)

            employee_todos = {str(id): list_todos}

        all_employees.update(employee_todos)

        name_file_json = 'todo_all_employees.json'

        with open(name_file_json, mode='w', newline='') as file:
            json.dump(all_employees, file)


if __name__ == '__main__':
    main()
