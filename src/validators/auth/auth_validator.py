from cerberus import Validator
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
"""
    {
        "username": "User",
        "password": "=password"
    }
"""


def auth_validator(request: any) -> None:
    body_validator = Validator({
        "username": {"type": "string", "required": True, "empty": False},
        "password": {"type": "string", "required": True, "empty": False}
    })

    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)