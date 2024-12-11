import json
import os


# File to store tasks
TASK_FILE = "tasks.json"


# Load tasks from file
def load_tasks():
    # Check if the File Exists
    if not os.path.exists(TASK_FILE):
        print("""The file "tasks.json" does not exsist. 
              Please create the file or contact administrator.""")
        return []
    # JSON ERROR HANDLE
    try:
        # If the file exist load the data from a tasks.json
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        return []
    

# Save tasks to file
def save_tasks(tasks):
    try:
        with open(TASK_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
    # If there is an error with writing to file (e.g., lack of disk space)
    except IOError as e:
        print(f"Error saving tasks: {e}")


# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    priority = input("Enter priority (low/medium/high): ")
    tasks.append({
        "title": title,
        "description": description,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully!")


# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, task in enumerate(tasks, start=1):
         status = "✔" if task["completed"] else "✘"
         print(f"{i}. [{status}] {task['title']} (Priority: {task['priority']})")
         print(f"   Description: {task['description']}")


# Update a task
def update_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task number to update: ")) - 1
    if 0 <= task_id < len(tasks):
        # This switches the value from one to another (from True to False and vice versa)
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
        print("Task updated successfully!")
    else:
        print("Invalid task number!")


# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        # Using pop to delete task from a list
        tasks.pop(task_id)
        print("task deleted successfully!")
    else:
        print("Invalid task number!")

# Reassign a task id
def reassign_task_ids(tasks):
    """
    Reassigns task IDs sequentially starting from 1.
    """
    for index, task in enumerate(tasks, start=1):
        task["id"] = index
