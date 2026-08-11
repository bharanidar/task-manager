from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

tasks = []


@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    task = {
    "id": len(tasks) + 1,
    "title": data["title"],
    "assigned_role": data["assigned_role"],
    "status": "pending"
}

    tasks.append(task)

    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = data["status"]
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)