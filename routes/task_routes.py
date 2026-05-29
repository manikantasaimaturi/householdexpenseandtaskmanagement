from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from services.task_service import (
    create_task_service,
    get_task_service,
    update_task_service,
    patch_task_service,
    delete_task_service
)

task_bp = Blueprint('task', __name__)


@task_bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():

    return create_task_service(request)


@task_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():

    return get_task_service()


@task_bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):

    return update_task_service(id, request)


@task_bp.route('/tasks/<int:id>', methods=['PATCH'])
@jwt_required()
def patch_task(id):

    return patch_task_service(id, request)


@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):

    return delete_task_service(id)