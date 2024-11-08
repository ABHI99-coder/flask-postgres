from flask import Blueprint, request, redirect, url_for, render_template
from todo.models import Task, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.complete = True
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/unmark/<int:task_id>', methods=['POST'])
def unmark_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.complete = False  # Unmark the task
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)  # Delete the task
        db.session.commit()
    return redirect(url_for('main.index'))


