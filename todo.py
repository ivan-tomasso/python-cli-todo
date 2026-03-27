import json
import os
from typing import List

TODO_FILE = "tasks.json"


def clear_screen() -> None:
    """Clears the terminal screen depending on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause() -> None:
    """Pauses execution until user presses Enter."""
    input("\nPress Enter to continue...")


def load_tasks() -> List[str]:
    """
    Loads tasks from a JSON file.

    Returns:
        A list of tasks. Returns an empty list if the file does not exist,
        is invalid, or cannot be read.
    """
    if not os.path.exists(TODO_FILE):
        return []

    try:
        with open(TODO_FILE, "r") as file:
            data = json.load(file)

            # Validate that the data is actually a list
            if isinstance(data, list):
                return data
            else:
                print("Warning: Invalid data format in file. Resetting tasks.")
                return []

    except json.JSONDecodeError as e:
        print(f"Warning: JSON file is corrupted: {e}")
        return []

    except OSError as e:
        print(f"Error reading file: {e}")
        return []


def save_tasks(tasks: List[str]) -> bool:
    """
    Saves the list of tasks to a JSON file.

    Returns:
        True if successful, False otherwise.
    """
    try:
        with open(TODO_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
        return True

    except OSError as e:
        print(f"Error saving file: {e}")
        return False


def display_tasks(tasks: List[str]) -> None:
    """Displays all current tasks."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\nCurrent Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task(tasks: List[str]) -> None:
    """Adds a new task to the list."""
    new_task = input("\nEnter the new task: ").strip()

    if not new_task:
        print("Error: Task cannot be empty.")
        return

    tasks.append(new_task)

    if save_tasks(tasks):
        print("Task added successfully.")
    else:
        print("Task added, but failed to save to file.")


def remove_task(tasks: List[str]) -> None:
    """Removes a task by index."""
    if not tasks:
        print("\nNo tasks to remove.")
        return

    try:
        task_index = int(input("\nEnter task number to remove: ")) - 1

        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)

            if save_tasks(tasks):
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Task removed, but failed to save changes.")
        else:
            print("Error: Task number out of range.")

    except ValueError:
        print("Error: Please enter a valid number.")


def main() -> None:
    """Main application loop."""
    tasks = load_tasks()

    try:
        while True:
            clear_screen()

            print("--- CLI To-Do List ---")
            print("1. View tasks")
            print("2. Add a task")
            print("3. Remove a task")
            print("4. Exit")

            choice = input("\nSelect an option (1-4): ").strip()

            if choice == "1":
                display_tasks(tasks)
                pause()

            elif choice == "2":
                add_task(tasks)
                pause()

            elif choice == "3":
                remove_task(tasks)
                pause()

            elif choice == "4":
                print("\nExiting program. Goodbye!")
                break

            else:
                print("\nError: Invalid choice.")
                pause()

    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()