from flask import jsonify

from config.database import db
from models.task_model import Task


def create_task_service(request):

    data = request.get_json()

    task = Task(
        title=data.get('title')
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({
        "message": "Task created"
    })


def get_task_service():

    tasks = Task.query.all()

    output = []

    for task in tasks:

        output.append({
            "id": task.id,
            "title": task.title,
            "status": task.status
        })

    return jsonify(output)


def update_task_service(id, request):

    data = request.get_json()

    task = Task.query.get(id)

    if not task:
        return {"message": "Task not found"}, 404

    task.title = data.get("title")
    task.description = data.get("description")
    task.status = data.get("status")

    db.session.commit()

    return {"message": "Task updated"}


def patch_task_service(id, request):

    task = Task.query.filter_by(id=id).first()

    if not task:

        return jsonify({
            "message": "Task not found"
        }), 404

    data = request.get_json()

    if 'title' in data:
        task.title = data['title']

    if 'status' in data:
        task.status = data['status']

    db.session.commit()

    return jsonify({
        "message": "Task partially updated"
    })


def delete_task_service(id):

    task = Task.query.filter_by(id=id).first()

    if not task:

        return jsonify({
            "message": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted"
    })