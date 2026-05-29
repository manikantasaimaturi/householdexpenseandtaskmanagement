from config.database import db


class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    expense_name = db.Column(db.String(100))

    amount = db.Column(db.Float)

    paid_by = db.Column(db.String(100))

    user_id = db.Column(db.Integer)