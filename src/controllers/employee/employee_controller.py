from typing import Dict, Union
from src.database.database import get_connect
from src.main.domain.models.models import Users
from src.main.domain.models.models import Employees
from src.main.domain.models.models import UsersRoles


class EmployeeController:


    def create(self, employee: dict) -> Dict:
        try:
            db = get_connect()

            new_user = Users.create(
                full_name=employee.get('full_name'),
                email=employee.get('email'),
                cpf=employee.get('cpf'),
                smartphone=employee.get('smartphone'),
                password=employee.get('password'),
                role_id=1
            )
            new_user.set_password(employee.get('password'))
            new_user.save()
            print(new_user.password)
            print(new_user)
            new_employee = Employees.create(
                user=new_user,
                departament=employee.get('departament'),
                salary=int(employee.get('salary')* 1000)
            )

            role_id_for_users_roles = 1  # replace with the correct role_id

            # Create UsersRoles instance with user_id and role_id
            users_roles_instance = UsersRoles.create(
                user_id=new_user.id,
                role_id=role_id_for_users_roles
            )

            id = new_employee.id
            new_employee.save()
            return self.__format(id)
        except Exception as e:
            print(e)


    def __format(self, id_created_product: str) -> Dict:
        return {
            "data": {
                "id": id_created_product
            }
        }

    def find_by_id_view(self, id: str) -> Union[Dict, None]:
        try:
            query = Employees.select().join(Users).where(Employees.id == id).first()
            employee = query
            if employee:
                return {"employee": employee.serialize()}  # Assuming you have a to_dict method in your model
            else:
                return {"error": "Employee not found"}, 404
        except Exception as e:
            print(e)
            return {"error": str(e)}, 500


    def one_delete(self, id: str) -> Dict:
        try:

            db = get_connect()
            query = Employees.select().join(Users).where(Employees.id == id).first()
            employee = query.serialize()

            id_employee_deleted = employee.get('id')

            user = Users.get(Users.id == employee.get('user_id').get('id'))


            if not employee:
                raise(f"Not found employee !")
            query_delete = Employees.delete().where(Employees.id == id)
            query_delete.execute()

            user_role_delete = UsersRoles.delete().where(UsersRoles.user_id == user)
            user_role_delete.execute()

            return {"id": id_employee_deleted}

        except Exception as e:
            print(e)





    @staticmethod
    def find_all() -> Dict:

        try:
            with get_connect():
                employees = Employees.select().join(Users)
                return {"employees: ": [{**employee.serialize(), "salary": "{:.2f}".format(employee.salary / 1000)} for employee in employees]}
        except Exception as e:
            print(e)
