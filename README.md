# procedural-cli-todo

A minimalist, multi-file command-line task management application written in pure, procedural Python. 

This project requires **zero third-party dependencies**, uses no serialized object libraries (such as `json` or `pickle`), and avoids custom function definitions (`def`). Execution flows cleanly across isolated scripts using core file-streaming execution.

---

## Table of Contents
1. [Architecture & Design](#architecture--design)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [User Manual](#user-manual)
   - [Launching the App](#launching-the-app)
   - [Viewing Tasks](#1-view-tasks)
   - [Adding Tasks](#2-add-a-task)
   - [Deleting Tasks](#3-delete-a-task)
   - [Saving and Exiting](#4-save-and-exit)
6. [Data Storage](#data-storage)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)

---

## Architecture & Design

Most starter projects bundle code into high-level abstractions or monolithic single-file scripts. **`procedural-cli-todo`** isolates individual program behaviors into separate files while retaining absolute procedural simplicity:

* **No Functions (`def`):** Code executes straight down in procedural blocks.
* **No `json` / External Libraries:** Relies on plain-text stream parsing with basic Python file I/O operations (`open`, `read`, `write`, `close`).
* **Modular Runtime:** `main.py` maintains state (`tasks` list) and dispatches lifecycle events into individual script files via `exec()`.

---

## Project Structure

```text
procedural-cli-todo/
├── .gitignore          # Ignores runtime storage and cache files
├── README.md           # Project documentation and user manual
├── main.py             # Application entry point and menu loop
├── load_tasks.py       # Reads lines from tasks.txt on startup
├── view_tasks.py       # Formats and prints current tasks to the terminal
├── add_task.py         # Handles user input and appends to task list
├── delete_task.py      # Validates index and pops task from list
└── save_tasks.py       # Serializes task list to tasks.txt and terminates
# procedural-cli-todo
