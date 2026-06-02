from flask import jsonify

from config.database import db
from models.expense_model import Expense


def create_expense_service(request):

    data = request.get_json()

    expense = Expense(
        expense_name=data.get('expense_name'),
        amount=data.get('amount'),
        paid_by=data.get('paid_by')
    )

    db.session.add(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense added"
    })


def get_expense_service():

    expenses = Expense.query.all()

    output = []

    for expense in expenses:

        output.append({
            "id": expense.id,
            "expense_name": expense.expense_name,
            "amount": expense.amount,
            "paid_by": expense.paid_by
        })

    return jsonify(output)


def update_expense_service(id, request):

    expense = Expense.query.filter_by(id=id).first()

    if not expense:

        return jsonify({
            "message": "Expense not found"
        }), 404

    data = request.get_json()

    expense.expense_name = data.get('expense_name')
    expense.amount = data.get('amount')
    expense.paid_by = data.get('paid_by')

    db.session.commit()

    return jsonify({
        "message": "Expense fully updated"
    })


def patch_expense_service(id, request):

    expense = Expense.query.filter_by(id=id).first()

    if not expense:

        return jsonify({
            "message": "Expense not found"
        }), 404

    data = request.get_json()

    if 'expense_name' in data:
        expense.expense_name = data['expense_name']

    if 'amount' in data:
        expense.amount = data['amount']

    if 'paid_by' in data:
        expense.paid_by = data['paid_by']

    db.session.commit()

    return jsonify({
        "message": "Expense partially updated"
    })


def delete_expense_service(id):

    expense = Expense.query.filter_by(id=id).first()

    if not expense:

        return jsonify({
            "message": "Expense not found"
        }), 404

    db.session.delete(expense)
    db.session.commit()

    return jsonify({
        "message": "Expense deleted"
    })