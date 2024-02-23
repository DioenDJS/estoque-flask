from flask import Blueprint, jsonify, request
from src.controllers.auth.auth_controllers import AuthController

auth_bp = Blueprint('auth', __name__)


@auth_bp.post('/register')
def register_user():
    return jsonify({"message": "User created"})


@auth_bp.post('/login')
def login():

    resp = None
    try:
        user_name = request.json.get('username')
        password = request.json.get('password')

        user_auth = AuthController()

        access_token = user_auth.auth_token(user_name, password)
        print(f"Username: {user_name}, Password: {password}, Access Token: {access_token}")
        resp = jsonify(access_token=access_token), 200
    except Exception as e:
        resp = jsonify({"error": "Credenciais inválidas"}), 401
    return resp
