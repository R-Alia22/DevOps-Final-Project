from flask import Flask, request, render_template_string

app = Flask(__name__)

tasks = []

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Final Project</title>
</head>
<body>
    <h1>Student Task Manager</h1>
    <p>This is a simple Flask application for my DevOps final project.</p>

    <form method="POST">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add Task</button>
    </form>

    <h2>Tasks:</h2>
    <ul>
        {% for task in tasks %}
            <li>{{ task }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
    return render_template_string(html_page, tasks=tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)