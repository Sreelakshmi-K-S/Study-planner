
const tasks = [
  { id: 1, task: "Complete Math Homework", completed: false },
  { id: 2, task: "Start Science Project", completed: false },
  { id: 3, task: "Attend English Class", completed: true },
];

const timetable = [
  { day: "Monday", time: "9:00 AM - 10:00 AM", subject: "Math" },
  { day: "Monday", time: "10:30 AM - 11:30 AM", subject: "Science" },
  { day: "Tuesday", time: "9:00 AM - 10:00 AM", subject: "English" },
  { day: "Tuesday", time: "10:30 AM - 11:30 AM", subject: "History" },
  { day: "Wednesday", time: "9:00 AM - 10:00 AM", subject: "Geography" },
  { day: "Wednesday", time: "10:30 AM - 11:30 AM", subject: "Computer Science" },
];

// Function to render tasks
function renderTasks() {
  const taskList = document.getElementById("todo-list");
  taskList.innerHTML = "";
  tasks.forEach((task) => {
    const taskElement = document.createElement("li");
    taskElement.innerHTML = `
      <input type="checkbox" ${task.completed ? "checked" : ""}>
      <span ${task.completed ? "style='text-decoration: line-through;'" : ""}>${task.task}</span>
      <button class="delete-btn">Delete</button>
    `;
    taskList.appendChild(taskElement);
  });
}

// Function to add new task
function addTask() {
  const taskInput = document.getElementById("task-input");
  const newTask = {
    id: tasks.length + 1,
    task: taskInput.value,
    completed: false,
  };
  tasks.push(newTask);
  taskInput.value = "";
  renderTasks();
}

// Function to delete task
function deleteTask(event) {
  const taskId = event.target.parentNode.dataset.taskId;
  tasks = tasks.filter((task) => task.id !== parseInt(taskId));
  renderTasks();
}

// Function to toggle task completion
function toggleTaskCompletion(event) {
  const taskId = event.target.parentNode.dataset.taskId;
  tasks = tasks.map((task) => {
    if (task.id === parseInt(taskId)) {
      task.completed = !task.completed;
    }
    return task;
  });
  renderTasks();
}

// Function to render timetable
function renderTimetable() {
  const timetableElement = document.getElementById("timetable");
  timetableElement.innerHTML = "";
  timetable.forEach((timetableEntry) => {
    const timetableRow = document.createElement("tr");
    timetableRow.innerHTML = `
      <td>${timetableEntry.day}</td>
      <td>${timetableEntry.time}</td>
      <td>${timetableEntry.subject}</td>
    `;
    timetableElement.appendChild(timetableRow);
  });
}

// Event listeners
document.getElementById("add-task-btn").addEventListener("click", addTask);
document.getElementById("todo-list").addEventListener("click", (event) => {
  if (event.target.classList.contains("delete-btn")) {
    deleteTask(event);
  } else if (event.target.type === "checkbox") {
    toggleTaskCompletion(event);
  }
});

// Initial render
renderTasks();
renderTimetable();