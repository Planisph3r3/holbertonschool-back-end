#!/usr/bin/python3
"""Using a mock api for fetch information"""
import requests
from sys import argv


def main():
    """Requesting the name and the todos of an enployee"""
    if len(argv) < 2:
        return "Missing/incorrect prompt parameter"
    employee_id: int = argv[1]
    url_name = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    request_employee_name = requests.get(url_name)
    url_employee_todos = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    request_employee_todos = requests.get(url_employee_todos)

    if request_employee_name.status_code == 200:
        employee_info_dict = request_employee_name.json()
        EMPLOYEE_NAME: str = employee_info_dict.get("name")
    else:
        print("Cannot fetch data")

    if request_employee_todos.status_code == 200:
        employee_todos_dict = request_employee_todos.json()
        TOTAL_NUMBER_OF_TASKS = len(employee_todos_dict)
        completed_tasks: list[any] = [
            each_todo for each_todo
            in employee_todos_dict if each_todo["completed"]
        ]
        NUMBER_OF_DONE_TASKS = len(completed_tasks)
    else:
        print("Cannot fetch data")

    print(
        f"Employee {EMPLOYEE_NAME} is done with "
        f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )

    for each_completed_task in completed_tasks:
        print(f"\t {each_completed_task["title"]}")


if __name__ == "__main__":
    main()

