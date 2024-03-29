from cerberus import Validator

"""
    VALIDAR OBJETO EMPLOYEE
    {
        full_name = "Nome completo do usuario"
        email = "usuarioemail@gmail.com"
        cpf = "00000000000"
        smartphone = "5399999999"
        password = "senhausuario"
        department: "MANAGER" 
        salary: 1579.00
    }
"""


def employee_creator_validator(request: any) -> None:
    body_validator = Validator({
        "full_name": {"type": "string", "required": True, "empty": False},
        "email": {"type": "string", "required": True, "empty": False, "regex": r'^\S+@\S+\.\S+$'},
        "cpf": {"type": "string", "required": True, "empty": False, "regex": r'^\d{11}$'},
        "smartphone": {"type": "string", "required": True, "empty": False, "regex": r'^\d{11}$'},
        "password": {"type": "string", "required": True, "empty": False},
        "department": {"type": "string", "required": True, "empty": False},
        "salary": {"type": "float", "required": True, "empty": False},
    })
    response = body_validator.validate(request.json)
    print(response)
    if response is False:
        raise Exception(body_validator.errors)