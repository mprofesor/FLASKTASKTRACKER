from flask import Flask, render_template, request, jsonify
from task_manager import load_tasks, save_tasks, reassign_task_ids

app = Flask(__name__)

# Route: Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Route: Get Tasks (API)
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

# Route: Add Task (API)
@app.route("/api/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks() # Load the current tasks

    # Generate a new unique task id by finding the highest existing id and adding 1
    new_task_id = max([task["id"] for task in tasks], default = 0) + 1

    # Get the new task data from the request body
    new_task = request.json
    new_task["id"] = new_task_id # Add the generated id to the new task

    # Append the new task to the tasks list
    tasks.append(new_task)
    
    # Save the updated tasks back to the file
    save_tasks(tasks)
    return jsonify({"message": "Task added successfully!"}), 201


# Route: Update Task (API)
# NEED TO CHANGE THE SEARCH TO SPECIFIC ID 
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks() # Load the current list of tasks


    # Find the task with the matching ID
    task_to_update = next((task for task in tasks if task["id"] == task_id), None)

    if task_to_update is None:
        # If no task is found with the given id, return 404
        return jsonify({"error": "Task not found"}), 404
    
    # Toggle the 'completed' status of the task
    task_to_update["completed"] = not task_to_update["completed"]

    # Save the updated tasks back to the file
    save_tasks(tasks)

    # Return a success message with the updated task
    return jsonify({"message": "Task updated successfully!", "task": task_to_update}), 200
    

# Route: Delete Task (API)
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks() # Load the current list of tasks

    # Find the task with the matching ID
    task_to_delete = next((task for task in tasks if task["id"] == task_id), None)

    if task_to_delete is None:
        # If no task is found with the given id, return 404
        return jsonify({"message": "Task not found!"}), 404
    
    # Remove the task with the matching id
    tasks = [task for task in tasks if task["id"] != task_id]

    # Reassign IDs to remaining tasks
    reassign_task_ids(tasks)

    # Save the updated tasks back to the file
    save_tasks(tasks)


    # Return a success message along with the deleted task data
    return jsonify({"message": "Task deleted successfully!", "task": task_to_delete}), 200



if __name__ == "__main__":
    app.run(debug=True)
