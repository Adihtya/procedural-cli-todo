# procedural-cli-todo

A minimalist, multi-file command-line interface (CLI) task manager engineered entirely in pure, procedural Python.

This project uses **zero third-party libraries**, completely avoids serialized data interchange formats (such as `json`, `yaml`, or `pickle`), and requires no function declarations (`def`) or object-oriented classes (`class`). It demonstrates how modular architecture and clean state management can be implemented in elementary Python using native file streaming and isolated script delegation.

---

## Badges & Highlights

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none-brightgreen.svg)
![Paradigm](https://img.shields.io/badge/paradigm-procedural-orange.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

* **Zero Dependencies:** Runs on standard, vanilla Python straight out of the box.
* **Modular Multi-File Design:** Each CRUD operation resides in its own isolated script file.
* **Pure Procedural Code:** No definitions (`def`), lambdas, or class structures—ideal for beginners and code anatomy demonstrations.
* **Clean File Persistence:** Uses newline-delimited standard I/O storage (`tasks.txt`).

---

## Table of Contents

1. [Architectural Overview](#architectural-overview)
2. [Repository File Tree](#repository-file-tree)
3. [Prerequisites](#prerequisites)
4. [Installation & Setup](#installation--setup)
5. [Detailed User Manual](#detailed-user-manual)
   - [Starting the Application](#starting-the-application)
   - [1. View Current Tasks](#1-view-current-tasks)
   - [2. Add a Task](#2-add-a-task)
   - [3. Delete a Task](#3-delete-a-task)
   - [4. Save and Exit](#4-save-and-exit)
6. [Data Storage Format](#data-storage-format)
7. [Edge Cases & Error Handling](#edge-cases--error-handling)
8. [Troubleshooting Guide](#troubleshooting-guide)
9. [Contributing](#contributing)
10. [License](#license)

---

## Architectural Overview

Most starter CLI tools either consolidate all logic into an unreadable monolithic script or rely heavily on advanced language constructs (`argparse`, classes, nested dictionaries, closures). 

**`procedural-cli-todo`** takes an alternative architectural approach:
* **Central Orchestrator (`main.py`):** Holds the in-memory array `tasks = []` and executes an interactive infinite loop (`while True`).
* **Sub-module Execution via `exec()`:** Operations (`load_tasks.py`, `view_tasks.py`, `add_task.py`, `delete_task.py`, `save_tasks.py`) run inside the caller's global variable scope using Python's native `exec(open(...).read())`.
* **Isolated Responsibilities:** Each script is strictly responsible for one atomic operational task:
  - Reading the disk
  - Mutating state
  - Rendering output
  - Serializing state back to disk

---

## Repository File Tree

```text
procedural-cli-todo/
├── .gitignore          # Prevents tracking runtime artifacts and storage
├── README.md           # Master documentation and operations manual
├── LICENSE             # Project distribution license (MIT)
├── main.py             # Entry point: runs loop and coordinates sub-scripts
├── load_tasks.py       # Reads lines from tasks.txt into tasks list
├── view_tasks.py       # Iterates through tasks and displays 1-based indexing
├── add_task.py         # Takes user input, validates, and appends task
├── delete_task.py      # Checks indices and safely pops chosen task
└── save_tasks.py       # Writes tasks line-by-line to tasks.txt
