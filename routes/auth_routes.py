from flask import Blueprint, request, jsonify

from services.auth_service import signup_user, login_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():

    return signup_user(request)


@auth_bp.route('/login', methods=['POST'])
def login():

    return login_user(request)