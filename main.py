from tasks import Task, TodoList


todo_list = TodoList()
    
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. mark as completed")
    print("4. change the priority")
    print("5. View Tasks")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        description = input("Enter task description: ")
        due_date = input("Enter due date (optional): ")
        try : 
            priority = int(input("Enter priority (1-5): "))
            if priority > 5 or priority < 1 :
                raise ValueError
            todo_list.add_task(description, due_date, priority)
        except ValueError :
            print ("priority must be intiger and betwwn 1 to 5")
    elif choice == '2':
        if not bool(len(todo_list.tasks)) :
            print("there is nothing in TodoList")
            continue
        todo_list.view_tasks()
        try :
            task_id = int(input("Enter task ID to remove: "))
            todo_list.remove_task(task_id-1)
        except ValueError :
            print ("plese Enter task ID\n *** Task ID is postive intiger *** ")
    elif choice == '3':
        if not bool(len(todo_list.tasks)) :
            print("there is nothing in TodoList")
            continue
        todo_list.view_tasks()
        try :
            task_id = int(input("Enter task ID to mark as completed: "))
            todo_list.mark_complete(task_id -1 )
        except ValueError :
            print ("plese Enter task ID\n *** Task ID is postive intiger *** ")
    elif choice == '4':
        if not bool(len(todo_list.tasks)) :
            print("there is nothing in TodoList")
            continue
        todo_list.view_tasks()
        try :
            task_id = int(input("Enter task ID to change priority: "))
            priority = int(input("Enter priority (1-5): "))
            if priority > 5 or 1> priority :
                raise ValueError
            todo_list.change_priority(task_id -1 ,priority)
        except ValueError :
            print ("plese Enter task ID\n *** Task ID is postive intiger *** \n ***priority must be between 1 to 5 ***")
    elif choice == '5':
        todo_list.view_tasks()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")