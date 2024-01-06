tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    if task.index == 0:
        task.index += 1
        print(f"task '{task}' added to the list.")
    else:
        print(f"task '{task}' added to the list.")
def listTasks():
    if not tasks:
        print("All Done! have a good day :)")
    else:
        print("Left to-Do")
        for index, task in enumerate(tasks):
            print(f"Task#{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Choose the Task Number to Delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print('invalid input.')
if __name__ == "__main__":
    print("Welcome to the todo list app :)")
    while True:
        print("\n")
        print("Please select below")
        print("\n")
        print('1. Add a task')
        print('2. Delete a task')
        print('3. List tasks')
        print("4. Quit")
        choice = input("enter your choice: ")

        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print('please enter something else')
    print("See ya, later!")