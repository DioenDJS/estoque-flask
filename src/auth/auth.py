from flask import Blueprint, jsonify, request
from src.controllers.auth.auth_controller import AuthController
from src.validators.auth.auth_validator import auth_validator
from src.views.http_types.http_request import HttpRequest

auth_bp = Blueprint('auth', __name__)


@auth_bp.post('/register')
def register_user():
    return jsonify({"message": "User created"})


@auth_bp.post('/login')
def login():

    resp = None
    try:
        user_auth = AuthController()

        auth_validator(request)

        http_request = HttpRequest(body=request.json)

        access_token = user_auth.auth_token(http_request)
        resp = jsonify(access_token=access_token), 200
    except Exception as e:
        resp = jsonify({"error": "Credenciais inválidas"}), 401
    return resp
