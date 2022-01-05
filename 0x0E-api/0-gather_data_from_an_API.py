#!/usr/bin/python3
# returns information about an employees ID

import requests
import sys

if __name__ == "__main__":

    employee_id = (sys.argv[1])
    employee_name = ''
    tasks_title = []
    tasklist = []
    tasks_defeated = 0
    wumbo_id = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(employee_id))
    to_do_list = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.
        format(employee_id))
    employee_name = wumbo_id.json().get('name')
    tasklist = to_do_list.json()
    for task in tasklist:
        if task.get('completed') is True:
            tasks_title.append(task['title'])
            tasks_defeated += 1
    print(
        'Employee {} is done with tasks({}/{}):'
        .format(employee_name, (tasks_defeated), len(tasklist)))
    for x in tasks_title:
        print('\t {}'.format(task.get('title')))
