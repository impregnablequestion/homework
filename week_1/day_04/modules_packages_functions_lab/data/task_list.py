tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    uncompleted_tasks = []
    for item in list:
        if item["completed"]== False:
            uncompleted_tasks.append(item)
    return uncompleted_tasks

get_uncompleted_tasks(tasks)

## Get a list of completed tasks
def get_completed_tasks(list):
    completed_tasks = []
    for item in list:
        if item["completed"]== True:
            completed_tasks.append(item)
    return completed_tasks

get_completed_tasks(tasks)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    eligible_tasks = []
    for item in list:
        if item["time_taken"] >= time:
            eligible_tasks.append(item)
    return eligible_tasks

get_tasks_taking_at_least(tasks, 30)

## Find a task with a given description
def get_task_with_description(list, description):
    for item in list:
        if item["description"] == description:
            return item

# Extention (Function): 

# Get a list of tasks by status
def get_tasks_by_status(list, status):
    uncompleted_tasks = []
    for item in list:
        if item["completed"]== status:
            uncompleted_tasks.append(item)
    return uncompleted_tasks