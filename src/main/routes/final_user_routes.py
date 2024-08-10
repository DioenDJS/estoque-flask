from flask import request, jsonify, Blueprint
from src.views.http_types.http_request import HttpRequest
from src.controllers.auth.auth_controller import AuthController
from src.validators.final_user.final_user_validator import final_user_find_one_validator
from src.views.final_user_view.final_user_view import FinalUserView
from flask_jwt_extended import jwt_required


final_users_routes_bp = Blueprint('final_users_routes', __name__)

auth_controller = AuthController()


@final_users_routes_bp.route('/final_user/create', methods=["POST"])
def create_final_user():
    resp = None
    try:
        # final_users_physical_person_creator_validator(request)

        final_user_view = FinalUserView()

        http_request = HttpRequest(body=request.json)

        resp = final_user_view.validate_and_create_final_users_physical_person(http_request)

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@final_users_routes_bp.route('/final_user/update/<final_user_id>', methods=["PUT"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def update_final_user(final_user_id):
    resp = None
    try:
        # final_users_physical_person_update_validator(request)

        final_users_physical_person_view = FinalUserView()

        http_request = HttpRequest(body=request.json)

        resp = final_users_physical_person_view.final_users_physical_person_update(final_user_id, http_request)

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@final_users_routes_bp.route('/final_users', methods=["GET"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def get_final_users():
    resp = None
    try:
        final_users_view = FinalUserView()

        resp = final_users_view.get_final_users()

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@final_users_routes_bp.route('/final_user/<final_user_id>', methods=["GET"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def get_final_user(final_user_id):
    resp = None
    try:

        params = {"final_user_id": final_user_id}

        print(params)

        final_user_find_one_validator(params)

        final_users_physical_person_view = FinalUserView()

        http_request = HttpRequest(query_params=params)

        resp = final_users_physical_person_view.get_final_users_by_id(http_request)

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@final_users_routes_bp.route('/final_user/<final_user_id>', methods=["DELETE"])
@jwt_required()
@auth_controller.roles_required('ADMIN', 'CLIENT')
def delete_final_user(final_user_id):
    resp = None
    try:

        params = {"final_user_id": final_user_id}

        final_user_find_one_validator(params)

        final_users_view = FinalUserView()

        http_request = HttpRequest(query_params=params)

        resp = final_users_view.delete_final_users(http_request)

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]
