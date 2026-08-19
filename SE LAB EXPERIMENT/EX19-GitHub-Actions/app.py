from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Learn Docker", "completed": False},
    {"id": 2, "task": "Learn GitHub Actions", "completed": False}
]

@app.route("/")
def home():
    return "Flask Application - Experiment 19 is Running!"

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)