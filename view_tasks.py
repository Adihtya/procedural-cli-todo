if "tasks" not in globals():
    tasks = []

if len(tasks) == 0:
    print("\nYour to-do list is empty.")
else:
    print("\nYour Tasks:")
    index = 1
    for task in tasks:
        print(str(index) + ". " + task)
        index = index + 1

