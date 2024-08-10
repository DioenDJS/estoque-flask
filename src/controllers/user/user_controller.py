from src.main.domain.models.models import Users, Roles, UserRoleEnum
from typing import Dict
from src.database.database import get_connect
from src.main.domain.enums.AccessStatus import AccessStatusEnum
from src.controllers.address.address_controller import AddressController

class UserController:

    def create(self, user: dict) -> Dict:
        try:
            db = get_connect()
            address_controller = AddressController()

            with db.atomic():

                address_user = address_controller.create(user)
                new_user = Users.create(
                    full_name=user.get('full_name'),
                    email=user.get('email'),
                    cpf=user.get('cpf'),
                    smartphone=user.get('smartphone'),
                    password=user.get('password'),
                    address=address_user.get("data").get("id"),
                    validate_access=user.get("validate_access"),
                    verification_code=user.get('verification_code')
                )

                new_user.set_password(user.get('password'))

                role_enum = UserRoleEnum.get(user.get('roles'))
                role, _ = Roles.get_or_create(nome=role_enum.value)
                new_user.roles.add(role)


                new_user.save()

                return self.__format(new_user.id)
        except Exception as e:
            print(f"Error creating user: {str(e)}")

    def __format(self, id_created_user: str) -> Dict:
        return {
            "data": {
                "id": id_created_user
            }
        }


    def check_Validation_send_verification_code(self, validate: dict) -> Dict:
        result = self.__Validation_send_verification_code(validate.get('id'), validate.get('code'))
        return {"validate_code": result}

    def __Validation_send_verification_code(self, id: str, code: int) -> bool:
        try:
            if code:
                user, _ = Users.get_or_create(id=id)

                if not user:
                    raise('User not found ! ')

                if user.verification_code == code:
                    user.validate_access=AccessStatusEnum.ACTIVE.value
                    user.save()

            return True
        except Exception as e:
            print(e)