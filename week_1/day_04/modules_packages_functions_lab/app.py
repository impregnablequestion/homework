from modules.output import *
from modules.input import *
from data.task_list import *


while (True):
    print_menu() # ––– where is this function defined?
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_tasks_by_status(tasks, True))
    elif option == '3':
        print_list(get_tasks_by_status(tasks, False))
    elif option == '4':
        get_task_from_description(description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = int(input("Enter task duration: "))
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = input("Enter task description to search for: ")
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = input("Enter description: ")
        time_taken = int(input("Enter time taken: "))
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")