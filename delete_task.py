if "tasks" not in globals():
    tasks = []

if len(tasks) == 0:
    print("\nNo tasks to delete.")
else:
    index = 1
    for task in tasks:
        print(str(index) + ". " + task)
        index = index + 1

    task_num = input("Enter task number to delete: ")
    if task_num.isdigit():
        number = int(task_num)
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print("Deleted: " + removed)
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

