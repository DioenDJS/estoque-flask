from typing import Dict, Union
from src.database.database import get_connect
from src.main.domain.models.models import Users, Employees, UserRoleEnum, Roles
from peewee import IntegrityError


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

            )
            new_user.set_password(employee.get('password'))

            role_enum = UserRoleEnum.get(employee.get('roles'))
            role, _ = Roles.get_or_create(nome=role_enum.value)
            new_user.roles.add(role)
            new_user.save()

            new_employee = Employees.create(
                user=new_user.id,
                salary=int(employee.get('salary') * 1000)
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

    def find_by_id(self, id: str) -> Union[Dict, None]:
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
        db = get_connect()
        try:
            with db.atomic():
                employee = Employees.get_by_id(id)
                user = None
                employee_id_deleted = employee.id
                if employee:
                    user = employee.user
                    user_id = user.id
                    user.roles.clear()
                    through_model = Users.roles.get_through_model()
                    employee.delete_instance()
                    user.delete_instance()
                    through_model.delete().where(getattr(through_model, 'users_id') == user_id).execute()
                return {"id": employee_id_deleted}

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



