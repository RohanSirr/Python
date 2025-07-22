def menu():
    print("\n---- To-Do-List ----")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")                                   # a function to show the options 
    print("4. Delete Task")
    print("5. Quit")

def addTask(tasks):                                                 # a function to add the task 
    task = input("Enter a task: ")                              
    tasks.append({'task': task, 'done': False})
    print("Task added successfully")

def viewTask(tasks):                                                # a function to view the task
    if not tasks:
        print("No tasks available")
    else:
        print("\n---- Your Tasks ----")
        for idx, t in enumerate(tasks, 1):
            status = "Done" if t['done'] else "Not Done"
            print(f"{idx}. {t['task']} - {status}")

def markDoneTask(tasks):                                            # a function to mark the task as done
    viewTask(tasks)
    if not tasks:
        print("No tasks available")
    num = input("Enter Task no. to marks as done: ")
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            print("Wohoo!! Task marked as done")
        else:
            print("Invalid task number")
    else:
        print("Please enter a valid no. ")

def deleteTask(tasks):                                              # a function to delete the task
    viewTask(tasks)
    if not tasks:
        print("No Task available")
    num = input("Enter Task no. to delete: ")
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(tasks):
            deletedTask = tasks.pop(idx)
            print(f"Task {deletedTask['task']} deleted successfully")
        else:
            print("Invalid Task no. ")
    else:
        print("Please enter a valid no.")

def main():                                                          # Here is the main menu option where we choose the option
    tasks = []
    while True:
        menu()
        choice = input("Enter your Choice (1-5): ")
        if choice == '1':
            addTask(tasks)
        elif choice == '2':
            viewTask(tasks)
        elif choice == '3':
            markDoneTask(tasks)                                            
        elif choice == '4':
            deleteTask(tasks)
        elif choice == '5':
            print("Exiting the program. Have a Great Day")
            break
        else:
            print("Invalid choice. Please choose a valid option")

main()
