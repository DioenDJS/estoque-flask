from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView
from src.errors.error_handler import handle_errors
from src.validators.tag_creator_validator import tag_creator_validator

tags_routes_bp = Blueprint('tags_routes', __name__)


@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    resp = None
    try:
        tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)

        resp = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        resp = handle_errors(exception)
    return jsonify(resp.body), resp.status_code[0]
