from flask import Blueprint, render_template, request
from app.backend.ai import chatWithGerry

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        task_name = request.form["task_name"]
        deadline = request.form["deadline"]
        hours = request.form["hours"]
        response = chatWithGerry(task_name, deadline, hours)
    return render_template("tasks.html", response=response)

from app import app

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == "POST":
        task_name = request.form["task_name"]
        deadline = request.form["deadline"]
        description = request.form["description"]
        response = chatWithGerry(task_name, deadline, description)
    return render_template('index.html', response=response)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html')