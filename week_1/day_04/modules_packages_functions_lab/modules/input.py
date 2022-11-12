from data.task_list import *

def get_task_from_description(description):
    description = input("Enter task description to search for: ")
    return get_task_with_description(tasks, description)