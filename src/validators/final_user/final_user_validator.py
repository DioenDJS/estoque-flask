from cerberus import Validator

"""
    VALIDAR OBJETO FINAL USER CREATE
    {
        full_name = "Nome completo do usuario"
        email = "usuarioemail@gmail.com"
        cpf = "00000000000"
        smartphone = "5399999999"
        password = "senhausuario"
        street: "Duque de Caxias",
        city: "Rio Grande",
        state: "RS",
        number:1399,
        zip_code: "96211-410",
        complement: "Casa dos fundos",
        Neighborhood: "Cidade Nova"
    }
"""


def final_user_creator_validator(request: any) -> None:
    body_validator = Validator({
        "full_name": {"type": "string", "required": True, "empty": False},
        "email": {"type": "string", "required": True, "empty": False, "regex": r'^\S+@\S+\.\S+$'},
        "cpf": {"type": "string", "required": True, "empty": False, "regex": r'^\d{11}$'},
        "smartphone": {"type": "string", "required": True, "empty": False, "regex": r'^\d{11}$'},
        "password": {"type": "string", "required": True, "empty": False},
        "street": {"type": "string", "required": True, "empty": False},
        "city": {"type": "string", "required": True, "empty": False},
        "state": {"type": "string", "required": True, "empty": False},
        "number": {"type": "string", "required": True, "empty": False},
        "zip_code": {"type": "string", "required": True, "empty": False},
        "complement": {"type": "string", "required": True, "empty": False},
        "Neighborhood": {"type": "string", "required": True, "empty": False},
    })
    response = body_validator.validate(request.json)
    print(response)
    if response is False:
        raise Exception(body_validator.errors)


"""
    VALIDAR OBJETO FINAL USER LIST ONE
    {
        full_name = "Nome completo do usuario"
    }
"""

def final_user_find_one_validator(params: any) -> None:
    params_validator = Validator({
        "final_user_id": {"type": "string", "required": True, "empty": False},
    })

    response = params_validator.validate(params)