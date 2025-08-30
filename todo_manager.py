import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. List 2. Add 3. Complete 4. Delete 0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            print("Added.")
        elif choice == "3":
            list_tasks(tasks)
            idx = int(input("Task number to complete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx]["done"] = True
                save_tasks(tasks)
        elif choice == "4":
            list_tasks(tasks)
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()
