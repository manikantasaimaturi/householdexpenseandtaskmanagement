from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from services.expense_service import (
    create_expense_service,
    get_expense_service,
    update_expense_service,
    patch_expense_service,
    delete_expense_service
)

expense_bp = Blueprint('expense', __name__)


@expense_bp.route('/expenses', methods=['POST'])
@jwt_required()
def create_expense():

    return create_expense_service(request)


@expense_bp.route('/expenses', methods=['GET'])
@jwt_required()
def get_expenses():

    return get_expense_service()


@expense_bp.route('/expenses/<int:id>', methods=['PUT'])
@jwt_required()
def update_expense(id):

    return update_expense_service(id, request)


@expense_bp.route('/expenses/<int:id>', methods=['PATCH'])
@jwt_required()
def patch_expense(id):

    return patch_expense_service(id, request)


@expense_bp.route('/expenses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_expense(id):

    return delete_expense_service(id)