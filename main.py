import os


tasks = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(filename):
    script_path = os.path.join(BASE_DIR, filename)
    with open(script_path, "r", encoding="utf-8") as script_file:
        exec(script_file.read(), globals())


# Load initial tasks
run_script("load_tasks.py")

# Main menu loop
while True:
    print("\n--- SIMPLE TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        run_script("view_tasks.py")
    elif choice == "2":
        run_script("add_task.py")
    elif choice == "3":
        run_script("delete_task.py")
    elif choice == "4":
        run_script("save_tasks.py")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.")

