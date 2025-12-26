from flask import Flask, request, jsonify
import json

app = Flask(__name__)
FILE = "tasks.json"


def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(load_tasks())


@app.route("/tasks", methods=["POST"])
def create_task():
    tasks = load_tasks()
    data = request.json
    data["status"] = "ToDo"
    tasks.append(data)
    save_tasks(tasks)
    return jsonify(data), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404

    tasks[task_id].update(request.json)
    save_tasks(tasks)
    return jsonify(tasks[task_id])


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    if task_id >= len(tasks):
        return jsonify({"error": "Task not found"}), 404

    deleted = tasks.pop(task_id)
    save_tasks(tasks)
    return jsonify(deleted)


if __name__ == "__main__":
    app.run(debug=True)
