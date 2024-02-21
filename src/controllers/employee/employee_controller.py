from typing import Dict
from src.database.database import get_connect
from src.main.domain.models.models import User
from src.main.domain.models.models import Employee


class EmployeeController:


    def create(self, employee: dict) -> Dict:
        try:
            db = get_connect()

            new_user = User.create(
                full_name=employee.get('full_name'),
                email=employee.get('email'),
                cpf=employee.get('cpf'),
                smartphone=employee.get('smartphone'),
                password=employee.get('password')
            )
            new_user.set_password(employee.get('password'))
            new_user.save()
            print(new_user.password)
            print(new_user)
            new_employee = Employee.create(
                user=new_user,
                departament=employee.get('departament'),
                salary=int(employee.get('salary')* 1000)
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


    @staticmethod
    def find_all() -> Dict:

        try:
            with get_connect():
                employees = Employee.select().join(User)
                return {"employees: ": [{**employee.serialize(), "salary": "{:.2f}".format(employee.salary / 1000)} for employee in employees]}
        except Exception as e:
            print(e)
