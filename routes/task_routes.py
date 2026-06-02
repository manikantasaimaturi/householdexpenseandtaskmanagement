from flask import Blueprint, request

from services.task_service import (
    create_task_service,
    get_task_service,
    update_task_service,
    patch_task_service,
    delete_task_service
)

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    """
    Create a new task
    ---
    tags:
      - Tasks
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
    responses:
      200:
        description: Task created successfully
      400:
        description: Invalid input
    """
    return create_task_service(request)


@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Get all tasks
    ---
    tags:
      - Tasks
    responses:
      200:
        description: List of tasks
    """
    return get_task_service()


@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    """
    Update a task completely
    ---
    tags:
      - Tasks
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            description:
              type: string
            status:
              type: string
    responses:
      200:
        description: Task updated successfully
      404:
        description: Task not found
    """
    return update_task_service(id, request)


@task_bp.route('/tasks/<int:id>', methods=['PATCH'])
def patch_task(id):
    """
    Partially update a task
    ---
    tags:
      - Tasks
    parameters:
      - name: id
        in: path
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Task updated partially
    """
    return patch_task_service(id, request)


@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    """
    Delete a task
    ---
    tags:
      - Tasks
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Task deleted successfully
    """
    return delete_task_service(id)