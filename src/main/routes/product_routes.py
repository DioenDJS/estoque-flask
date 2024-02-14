from flask import request, jsonify, Blueprint
from src.views.product_creator_view import ProductCreatorView
from src.validators.product_creator_validator import product_creator_validator
from src.views.http_types.http_request import HttpRequest


product_routes_bp = Blueprint('product_routes', __name__)


@product_routes_bp.route('/produto', methods=["POST"])
def create_product():
    resp = None
    try:
        product_creator_validator(request)
        product_creator_view = ProductCreatorView()

        http_request = HttpRequest(body=request.json)

        resp = product_creator_view.validate_and_create_product(http_request)
    except Exception as e:
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]