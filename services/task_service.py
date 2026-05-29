from flask import jsonify

from flask_jwt_extended import get_jwt_identity

from config.database import db

from models.task_model import Task


def create_task_service(request):

    current_user = get_jwt_identity()

    data = request.get_json()

    task = Task(
        title=data.get('title'),
        user_id=current_user
    )

    db.session.add(task)

    db.session.commit()

    return jsonify({
        "message": "Task created"
    })


def get_task_service():

    current_user = get_jwt_identity()

    tasks = Task.query.filter_by(user_id=current_user).all()

    output = []

    for task in tasks:

        output.append({
            "id": task.id,
            "title": task.title,
            "status": task.status
        })

    return jsonify(output)


def update_task_service(id, request):

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

    if not task:

        return jsonify({
            "message": "Task not found"
        }), 404

    data = request.get_json()

    task.title = data.get('title')

    task.status = data.get('status')

    db.session.commit()

    return jsonify({
        "message": "Task fully updated"
    })


def patch_task_service(id, request):

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

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

    current_user = get_jwt_identity()

    task = Task.query.filter_by(
        id=id,
        user_id=current_user
    ).first()

    if not task:

        return jsonify({
            "message": "Task not found"
        }), 404

    db.session.delete(task)

    db.session.commit()

    return jsonify({
        "message": "Task deleted"
    })