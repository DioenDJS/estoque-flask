from src.main.domain.models.models import Users, Roles
from typing import Dict
from src.database.database import get_connect


class UserController:

    def create(self, user: dict) -> Dict:
        try:
            db = get_connect()

            role_names = user.get('roles', [])

            with db.atomic():
                new_user = Users.create(
                    full_name=user.get('full_name'),
                    email=user.get('email'),
                    cpf=user.get('cpf'),
                    smartphone=user.get('smartphone'),
                    password=user.get('password')
                )

                new_user.set_password(user.get('password'))

                # Get or create roles and assign them to the user
                for role_name in role_names:
                    role, _ = Roles.get_or_create(nome=role_name)
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
