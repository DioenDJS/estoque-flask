from cerberus import Validator
"""
    {
        "name": "Caderno",
        "price": 1299,
        "description": "caderno de um materia"
        "tag": "432535234.4352435.png"
    }
"""


def product_creator_validator(request: any) -> None:
    body_validator = Validator({
        "name": {"type": "string", "required": True, "empty": False},
        "price": {"type": "integer", "required": True, "empty": False},
        "description": {"type": "string", "required": True, "empty": False},
        "tag": {"type": "string", "required": True, "empty": False},
    })

    response = body_validator.validate(request.json)
    print(response)
    if response is False:
        raise Exception(body_validator.errors)
