from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.employee.employee_controller import EmployeeController

class EmployeeView:


    def validate_and_create_employee(self, http_request: HttpRequest) -> HttpResponse:

        employee_controller = EmployeeController()

        body = http_request.body

        result = employee_controller.create(body)

        return HttpResponse(status_code=201, body=result)


    def find_all_view(self) -> HttpResponse:

        employee_controller = EmployeeController()

        result = employee_controller.find_all()

        return HttpResponse(status_code=200, body=result)
