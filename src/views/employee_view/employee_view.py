from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.employee.employee_controller import EmployeeController


class EmployeeView:
    employee_controller = EmployeeController()

    def validate_and_create_employee(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        result = self.employee_controller.create(body)

        return HttpResponse(status_code=201, body=result)


    def find_all_view(self) -> HttpResponse:

        result = self.employee_controller.find_all()

        return HttpResponse(status_code=200, body=result)


    def find_by_id(self, id: str) -> HttpResponse:

        result = self.employee_controller.find_by_id(id)

        return HttpResponse(status_code=200, body=result)


    def delete(self, id: str) -> HttpResponse:

        employee_controller = EmployeeController()

        result = employee_controller.one_delete(id)
        print(result)
        return HttpResponse(status_code=200, body=result)