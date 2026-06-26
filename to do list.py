tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            tasks[index] = new_task
            print("Task updated successfully!")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            index = int(input("Enter task number to delete: ")) - 1
            tasks.pop(index)
            print("Task deleted successfully!")

    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            index = int(input("Enter completed task number: ")) - 1
            tasks[index] = "✔ " + tasks[index]
            print("Task marked as completed!")

    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice!")