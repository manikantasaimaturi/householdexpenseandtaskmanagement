from flask import Blueprint, request

from services.expense_service import (
    create_expense_service,
    get_expense_service,
    update_expense_service,
    patch_expense_service,
    delete_expense_service
)

expense_bp = Blueprint('expense', __name__)


@expense_bp.route('/expenses', methods=['POST'])
def create_expense():
    """
    Create a new expense
    ---
    tags:
      - Expenses
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            amount:
              type: number
            category:
              type: string
    responses:
      200:
        description: Expense created successfully
      400:
        description: Invalid input
    """
    return create_expense_service(request)


@expense_bp.route('/expenses', methods=['GET'])
def get_expenses():
    """
    Get all expenses
    ---
    tags:
      - Expenses
    responses:
      200:
        description: List of expenses
    """
    return get_expense_service()


@expense_bp.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    """
    Update an expense completely
    ---
    tags:
      - Expenses
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
            amount:
              type: number
            category:
              type: string
    responses:
      200:
        description: Expense updated successfully
      404:
        description: Expense not found
    """
    return update_expense_service(id, request)


@expense_bp.route('/expenses/<int:id>', methods=['PATCH'])
def patch_expense(id):
    """
    Partially update an expense
    ---
    tags:
      - Expenses
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
        description: Expense updated partially
    """
    return patch_expense_service(id, request)


@expense_bp.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    """
    Delete an expense
    ---
    tags:
      - Expenses
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Expense deleted successfully
    """
    return delete_expense_service(id)