from flask import Blueprint, request

from services.auth_service import signup_user, login_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """
    User Signup
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: User created successfully
      400:
        description: Invalid input
    """
    return signup_user(request)


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Auth
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Login successful
      401:
        description: Invalid credentials
    """
    return login_user(request)