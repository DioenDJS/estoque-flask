from flask import request, jsonify, Blueprint
from src.views.product_view.product_view import ProductView
from src.validators.product_creator_validator import product_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.controllers.auth.auth_controllers import AuthController
from flask_jwt_extended import jwt_required, get_jwt_identity

product_routes_bp = Blueprint('product_routes', __name__)

auth_controller = AuthController()


@product_routes_bp.route('/produto', methods=["POST"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def create_product():
    resp = None
    try:
        product_creator_validator(request)
        product_view = ProductView()

        http_request = HttpRequest(body=request.json)

        resp = product_view.validate_and_create_product(http_request)
    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]


@product_routes_bp.route('/produtos', methods=["GET"])
@jwt_required()
@auth_controller.roles_required('ADMIN')
def get_all_product():
    current_user = get_jwt_identity()
    print(current_user)
    resp = None
    try:
        product_view = ProductView()
        products = product_view.find_all_product()
        resp = products
    except Exception as e:
        resp = jsonify({"error": str(e)}), 500

    return jsonify(resp.body), resp.status_code[0]

