document.addEventListener("DOMContentLoaded", () => {
    loadTasks();
});

function addTask() {
    const taskInput = document.getElementById("taskInput");
    if (taskInput.value.trim() === "") return;

    const taskList = document.getElementById("taskList");
    const li = document.createElement("li");
    li.className = "task-item";

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", toggleTask);

    const span = document.createElement("span");
    span.textContent = taskInput.value;

    const deleteBtn = document.createElement("span");
    deleteBtn.innerHTML = "🗑";
    deleteBtn.className = "delete-btn";
    deleteBtn.addEventListener("click", deleteTask);

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);

    saveTasks();
    taskInput.value = "";
}

function toggleTask(event) {
    const task = event.target.nextSibling;
    task.classList.toggle("completed", event.target.checked);
    saveTasks();
}

function deleteTask(event) {
    event.target.parentElement.remove();
    saveTasks();
}

function saveTasks() {
    const tasks = [];
    document.querySelectorAll(".task-item").forEach(taskItem => {
        tasks.push({
            text: taskItem.children[1].textContent,
            completed: taskItem.children[0].checked
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach(task => {
        const taskInput = document.getElementById("taskInput");
        taskInput.value = task.text;
        addTask();
        document.querySelector(".task-item:last-child input[type='checkbox']").checked = task.completed;
        document.querySelector(".task-item:last-child span").classList.toggle("completed", task.completed);
    });
}