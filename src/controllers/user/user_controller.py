from src.main.domain.models.models import Users
from typing import Dict
from src.database.database import get_connect

class UserController:

    def create(self, user: dict) -> Dict:
        try:
            db = get_connect()
            new_user = Users.create(
                full_name=user.get('full_name'),
                email=user.get('email'),
                cpf=user.get('cpf'),
                smartphone=user.get('smartphone'),
                password=user.get('password')
            )

            new_user.set_password(user.get('password'))

            id = new_user.id

            new_user.save()
            return self.__format(id)
        except Exception as e:
            print(f"Erro ao criar usuario {str(e)}")


    def __format(self, id_created_user: str) -> Dict:
        return {
            "data": {
                "id": id_created_user
            }
        }



