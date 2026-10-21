tasks = []

def add_task():
    task_name = input("Enter the task you want to add: ")
    tasks.append({"name": task_name, "done":False})
    print("Task added successfully! ")

def show_tasks():
    if not tasks:
        print("No tasks found!")
    else:
        for i, task in enumerate(tasks, 1):
            if task["done"]:
                status = "Done"
            else:
                status = "Pending"
            print(f"{i}. {task['name']} - {status}")

def mark_done():
    show_tasks()
    if not tasks:
        return
    task_number = int(input("Enter task number to mark as done: "))
    if task_number>=1 and task_number <=len(tasks):
        tasks[task_number-1]["done"] = True
        print("Task marked as done!")
    else:
        print("You have entered an incorrect number.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    delete_task_number = int(input("Enter task number to delete: "))
    if delete_task_number>=1 and delete_task_number <= len(tasks):
        deleted_task = tasks.pop(delete_task_number-1)
        print(f"Task deleted: {deleted_task['name']}")
    else:
        print("wrong task number entered.")

while True:
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter what task you want to perform out of (1/2/3/4/5): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        mark_done()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Thank you for using To-Do List! ")
        break

    else:
        print("Invalid choice! Please select from 1 to 5.")