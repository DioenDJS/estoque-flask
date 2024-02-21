from flask import jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.controllers.user.user_controller import UserController
from flask_jwt_extended import jwt_required

login_route = Blueprint('login', __name__)


@login_route.route('/login', methods=['POST'])
def login():

    resp = None
    try:
        # Lógica de autenticação
        # Verifique as credenciais do usuário e gere um token JWT se for bem-sucedido

        user_name = request.json.get('username')
        password = request.json.get('password')

        user_auth = UserController()

        access_token = user_auth.auth_token(user_name, password)

        resp = jsonify(access_token=access_token), 200
    except Exception as e:
        resp = jsonify({"error": "Credenciais inválidas"}), 401

    return resp

@login_route.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200