from flask import jsonify

from flask_bcrypt import Bcrypt

from config.database import db

from models.user_model import User

bcrypt = Bcrypt()


def signup_user(request):

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Signup successful"
    })


def login_user(request):

    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({
            "message": "Invalid username"
        }), 401

    if bcrypt.check_password_hash(user.password, password):
        return jsonify({
            "message": "Login successful"
        })

    return jsonify({
        "message": "Wrong password"
    }), 401