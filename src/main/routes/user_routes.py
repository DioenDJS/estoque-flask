from flask import request, jsonify, Blueprint
from src.validators.user_creator_validator import user_creator_validator
from src.views.http_types.http_request import HttpRequest
from src.views.user_view.user_view import UserView



user_routes_bp = Blueprint('user_routes', __name__)


@user_routes_bp.route('/user/created', methods=["POST"])
def create_user():
    resp = None
    try:
        user_view = UserView()
        user_creator_validator(request)

        http_request = HttpRequest(body=request.json)

        resp = user_view.validate_and_create_user(http_request)
    except Exception as e:
        print(e)
        resp = jsonify({"error": str(e)}), 500
    return jsonify(resp.body), resp.status_code[0]
