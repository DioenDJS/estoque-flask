import datetime

from src.database.database import get_connect
from datetime import datetime
from src.drivers.phonenumbers_handler import PhonenumbersHandler
from src.main.domain.enums.AccessStatus import AccessStatusEnum
from src.controllers.user.user_controller import UserController
from typing import Dict
from src.main.domain.models.models import (
    Users,
    FinalUsersPhysicalPerson
)
import random
import pytz


phonenumbers_handler = PhonenumbersHandler()
user_controller = UserController()


class FinalUserController:

    def create(self, final_users_physical_person: dict) -> Dict:

        db = get_connect()
        with db.atomic() as txn:
            try:

                verification_code = str(random.randint(1000, 9999))

                final_users_physical_person["verification_code"] = verification_code
                final_users_physical_person["validate_access"] = AccessStatusEnum.INACTIVE.value
                final_users_physical_person["roles"] = "CLIENT"

                new_user = user_controller.create(final_users_physical_person)

                new_final_users_physical_person = FinalUsersPhysicalPerson.create(
                    user=new_user.get('data').get('id'),
                )

                id = new_final_users_physical_person.id
                new_final_users_physical_person.save()
                txn.commit()
                phonenumbers_handler.generate_and_send_sms(final_users_physical_person.get('smartphone'), verification_code)
                return self.__format(id)
            except Exception as err:
                txn.rollback()
                print(err)

    def __format(self, id_created_product: str) -> Dict:
        return {
            "data": {
                "id": id_created_product
            }
        }


    def update(self, id: str, final_users_physical_person: dict) -> Dict:
        db = get_connect()
        with db.atomic() as txn:
            try:
                final_users_search = FinalUsersPhysicalPerson.get_by_id(id)

                if not final_users_search:
                    raise("FOUND NOT FINAL USER ")

                user_search = Users.get_by_id(final_users_search.user.id)

                for field, value in final_users_physical_person.items():
                    setattr(user_search, field, value)

                user_search.save()

                txn.commit()
                final_users_searchdois = FinalUsersPhysicalPerson.get_by_id(id)
                return {"final_user": final_users_searchdois.serialize()}
            except Exception as e:
                txn.rollback()
                print(e)

    def find_all(self) -> Dict:
        final_users = FinalUsersPhysicalPerson.select()
        active_final_users = [final_user.serialize() for final_user in final_users if final_user.serialize()['user']['validate_access'] == 'ACTIVE']
        return {
                "finalusers:": active_final_users
        }


    def find_by_id(self, id: str) -> Dict:
        final_user = FinalUsersPhysicalPerson.get_by_id(id)
        user_found = final_user.serialize()
        print(user_found)
        print(user_found['user']['validate_access'])
        if not final_user or user_found['user']['validate_access'] != 'ACTIVE':
            raise(f"FINAL USER NOT FOUND !")

        return {
            "finalusers:": final_user.serialize()
        }


    def one_delete(self, id: str) -> Dict:
        print("esta entrando aqiui ")
        db = get_connect()
        try:
            with db.atomic() as txn:
                final_user = FinalUsersPhysicalPerson.get_by_id(id)

                if not final_user:
                    raise(f"FINAL USER NOT FOUND !")

                final_user_id_deleted = final_user.id

                user = final_user.user
                address = user.address
                through_model = Users.roles.get_through_model()
                final_user.delete_instance()
                user.delete_instance()
                address.delete_instance()
                through_model.delete().where(getattr(through_model, 'users_id') == user.id).execute()
            txn.commit()
            return {"id": final_user_id_deleted}
        except Exception as e:
            print(e)


    def soft_delete(self, id: str) -> Dict:
        db = get_connect()
        try:
            with db.atomic() as txn:
                final_user = FinalUsersPhysicalPerson.get_by_id(id)
                if not final_user:
                    raise (f"FINAL USER NOT FOUND !")

                final_user_id_deleted = final_user.id
                user = Users.get_by_id(final_user.user.id)

                user.validate_access = AccessStatusEnum.BLOCKED.value
                user.verification_code = None
                user.password = ""
                user.deleted_at = datetime.now()

                user.save()
            txn.commit()
            return {"id": final_user_id_deleted}

        except Exception as e:
            print(e)
