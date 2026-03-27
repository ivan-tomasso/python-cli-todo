# Python CLI To-Do List

A simple, robust, and easy-to-use CLi To-Do List application written in core Python. 

This project was built as a foundational exercise to master fundamental programming concepts such as File I/O, error handling, modularity, and working with JSON data, without relying on external or heavy libraries.

## Features

- **Add, View, and Remove Tasks:** Core CRUD (Create, Read, Update, Delete) operations.
- **Persistent Storage:** Tasks are automatically saved to a local `tasks.json` file.
- **Cross-Platform:** The terminal screen clears smoothly on both Windows and macOS/Linux.
- **Robust Error Handling:** The application handles corrupted files, missing permissions (OSError), and unexpected user interruptions (`Ctrl+C`) gracefully.
- **Input Validation:** Prevents the creation of empty tasks and catches out-of-bounds removals.

## How to Run

Since this project uses only Python's standard library, there are no external dependencies to install.

**Prerequisites:**
- Python 3.6 or higher installed on your system.

**Steps:**
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/tivannn/python-cli-todo.git
