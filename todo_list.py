# Task-1

todo_list = []

def show_menu():
    print("\n---------------------------------")
    print("------- To-Do List Menu -------")
    print("---------------------------------")
    print("Select an option:")
    print("1️Show To-Do List Tasks")
    print("2️Add Task")
    print("3️Remove Task")
    print("4️Exit")

def show_tasks():
    if not todo_list:
        print("\n❌ No tasks in your to-do list.")
    else:
        print("\n---------------------------------")
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
        print("---------------------------------")

def add_task():
    task = input("\nEnter a task: ")
    todo_list.append(task)
    print("✅ Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("\nExiting.....")
        break
    else:
        print("Invalid choice. Please try again.")
