from src.main.domain.models.models import User
import bcrypt
from typing import Dict
from src.database.database import get_connect
from flask_jwt_extended import create_access_token
class UserController:

    def create(self, user: dict) -> Dict:
        try:
            db = get_connect()
            new_user = User.create(
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


    def auth_token(self, username: str, password: str):
        try:

            with get_connect():
                users = User.select().where(User.full_name == username)
                user = [user.serialize() for user in users]
                if not user:
                    raise Exception("User not found!")

                user_check_password = user[0]
                storage_hashed_passqword = user_check_password.get('password')
                storage_hashed_passqword_byte = storage_hashed_passqword.encode('utf-8')
                password_match = bcrypt.checkpw(password.encode('utf-8'), storage_hashed_passqword_byte)

                if password_match:
                    return create_access_token(identity=username)
                else:
                    print("Password is incorrect.")




        except Exception as e:
            print(e)
