from flask import request, jsonify, Blueprint
from src.views.http_types.http_request import HttpRequest
from src.views.employee_view.employee_view import EmployeeView
from src.controllers.auth.auth_controllers import AuthController
from flask_jwt_extended import jwt_required


employee_routes_bp = Blueprint('employee_routes', __name__)

auth_controller = AuthController()

@employee_routes_bp.route('/employee/create', methods=["POST"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def create_employee():
    resp = None
    try:
        employee_view = EmployeeView()

        http_request = HttpRequest(body=request.json)

        resp = employee_view.validate_and_create_employee(http_request)

    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@employee_routes_bp.route('/employees', methods=["GET"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def list_employee():
    resp = None
    try:
        employee_view = EmployeeView()

        resp = employee_view.find_all_view()
    except Exception as e:
        print(str(e))
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@employee_routes_bp.route('/employee/<string:id>', methods=["GET"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def list_by_id_employee(id):
    resp = None
    try:
        employee_view = EmployeeView()

        resp = employee_view.find_by_id(id)
    except Exception as e:
        print(e)
    return jsonify(resp.body), resp.status_code[0]


@employee_routes_bp.route('/employee/<string:id>', methods=["DELETE"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def delete_employee(id):
    resp = None
    try:
        employee_view = EmployeeView()

        resp = employee_view.delete(id)
    except Exception as e:
        print(e)
    return jsonify(resp.body), resp.status_code[0]