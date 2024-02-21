from flask import request, jsonify, Blueprint
from src.views.http_types.http_request import HttpRequest
from src.views.employee_view.employee_view import EmployeeView


employee_routes_bp = Blueprint('employee_routes', __name__)


@employee_routes_bp.route('/employee/create', methods=["POST"])
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
def list_employee():
    resp = None
    try:
        employee_view = EmployeeView()

        resp = employee_view.find_all_view()
    except Exception as e:
        print(str(e))
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]
