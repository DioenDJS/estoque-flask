from src.main.domain.models.models import Users
from src.views.http_types.http_response import HttpResponse
from src.views.http_types.http_request import HttpRequest
from src.database.database import get_connect
from flask import jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity
from functools import wraps


class AuthController:

    def auth_token(self, http_request: HttpRequest) -> HttpResponse:
        try:
            with get_connect():
                user, _ = Users.get_or_create(full_name=http_request.body.get("username"))
                if not user:
                    raise Exception("User not found!")

                user_check_password = user.check_password(http_request.body.get("password"))

                if user_check_password:
                    identity_data = {
                        'username': http_request.body.get("username"),
                        'roles': [role.nome for role in user.roles],
                    }
                    return create_access_token(identity=identity_data)
                else:
                    print("Password is incorrect.")
        except Exception as e:
            print(e)


    def roles_required(*required_roles):
        def decorator(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                verify_jwt_in_request()
                current_roles = get_jwt_identity().get('roles', [])

                if any(role in current_roles for role in required_roles):
                    return fn(*args, **kwargs)
                else:
                    return jsonify({"error": "Insufficient permissions"}), 403

            return wrapper

        return decorator
