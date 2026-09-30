import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.txt")

if "tasks" not in globals():
    tasks = []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass

with open(TASKS_FILE, "w", encoding="utf-8") as file:
    for task in tasks:
        file.write(task + "\n")

print("Tasks saved to tasks.txt. Goodbye!")

