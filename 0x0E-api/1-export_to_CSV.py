#!/usr/bin/python3
"""returns information about an employees ID"""

import requests
import sys
import csv

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
    f = open("{}.csv".format(employee_id), "w", newline='')
    spamwriter = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=",")
    for task in tasklist:
        spamwriter.writerow([employee_id, employee_name,
                            task.get('completed'), task.get('title')])
