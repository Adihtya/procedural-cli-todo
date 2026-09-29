if "tasks" not in globals():
    tasks = []

new_task = input("\nEnter task: ")
if new_task != "":
    tasks.append(new_task)
    print("Added: " + new_task)
else:
    print("Task cannot be empty.")

