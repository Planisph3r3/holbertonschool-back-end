#!/usr/bin/python3
"""Using a mock api for fetch information"""
import csv
import requests
from sys import argv, exit


def main():
    """Requesting the name and the todos of an enployee"""
    if len(argv) > 1 and argv[1].isdigit():
        employee_id: int = argv[1]
        url_name = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        request_employee_name = requests.get(url_name)
        url_employee_todos = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        )
        request_employee_todos = requests.get(url_employee_todos)

        if request_employee_name.status_code == 200:
            employee_info_dict = request_employee_name.json()
            EMPLOYEE_NAME: str = employee_info_dict.get("username")
        else:
            print("Cannot fetch data")
            exit()

        if request_employee_todos.status_code == 200:
            employee_todos_dict = request_employee_todos.json()
            TOTAL_NUMBER_OF_TASKS = len(employee_todos_dict)
            completed_tasks: list[any] = [
                each_todo for each_todo in employee_todos_dict
                if each_todo["completed"]
            ]
            NUMBER_OF_DONE_TASKS = len(completed_tasks)
        else:
            print("Cannot fetch data")
            exit()

        csv_data = []
        all_tasks: list[any] = [each_todo["title"]
                                for each_todo in employee_todos_dict]
        all_tasks_bool: list = [
            each_todo["completed"] for each_todo in employee_todos_dict
        ]
        for a in range(0, len(employee_todos_dict)):
            b = [str(employee_id), EMPLOYEE_NAME,
                 str(all_tasks_bool[a]), all_tasks[a]]
            csv_data.append(b)

        csv_file_path = f"{employee_id}.csv"

        with open(csv_file_path, mode="w", newline="") as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            writer.writerows(csv_data)
    else:
        print("Missing/incorrect prompt parameter")
        exit()


if __name__ == "__main__":
    main()
