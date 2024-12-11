async function fetchTasks() {
    const response = await fetch('/api/tasks');
    const tasks = await response.json();
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Clear the list

    tasks.forEach((task) => {
        const taskDiv = document.createElement('div');
        taskDiv.className = 'task';
        taskDiv.innerHTML = `
            <span class="${task.completed ? 'completed' : ''}">
                ${task.id}. ${task.title} (Priority: ${task.priority})
            </span>
            <button onclick="showDescription('${task.description}')">Toggle Description</button>
            <button onclick="toggleTask(${task.id})">Toggle Complete</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(taskDiv);
    });
}

// Function to add a new task
async function addTask(event) {
    event.preventDefault();
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-description').value;
    const priority = document.getElementById('task-priority').value;

    const newTask = { title, description, priority, completed: false };

    await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newTask),
    });

    fetchTasks();
}


// Function to toggle task completion status
async function toggleTask(taskId) {
    await fetch(`/api/tasks/${taskId}`, { method: 'PUT' });
    fetchTasks();
}

// Function to delete a task
async function deleteTask(taskId) {
    await fetch(`/api/tasks/${taskId}`, { method: 'DELETE'}); // Send DELETE request
    fetchTasks(); // Refresh task list after deletion
}


// Function to toggle the description
function showDescription(description) {
    const descriptionElement = document.getElementById('description-paragraph');

    // Toggle visibility and update content
    if (descriptionElement.classList.contains('hidden')) {
        descriptionElement.textContent = description;
        descriptionElement.classList.remove('hidden');
    }
    else {
        descriptionElement.textContent = '';
        descriptionElement.classList.add('hidden');
    }

}


// Fetch tasks when the page loads
fetchTasks();
