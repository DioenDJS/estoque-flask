from src.main.domain.models.models import Users
from src.database.database import get_connect
from flask import jsonify
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity
from functools import wraps
import bcrypt


class AuthController:

    def auth_token(self, username: str, password: str):
        try:

            with get_connect():
                users = Users.select().where(Users.full_name == username)
                user = [user.serialize() for user in users]
                if not user:
                    raise Exception("User not found!")

                user_check_password = user[0]
                storage_hashed_passqword = user_check_password.get('password')
                storage_hashed_passqword_byte = storage_hashed_passqword.encode('utf-8')
                password_match = bcrypt.checkpw(password.encode('utf-8'), storage_hashed_passqword_byte)

                if password_match:
                    identity_data = {
                        'username': username,
                        'roles': [user_check_password.get('role').get('nome')],
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
                verify_jwt_in_request()  # Ensure a valid JWT is present
                current_roles = get_jwt_identity().get('roles', [])

                # Check if the user has at least one of the required roles
                if any(role in current_roles for role in required_roles):
                    return fn(*args, **kwargs)
                else:
                    return jsonify({"error": "Insufficient permissions"}), 403

            return wrapper

        return decorator