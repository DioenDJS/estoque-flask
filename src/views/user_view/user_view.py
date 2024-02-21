from src.controllers.user.user_controller import UserController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class UserView:


    def validate_and_create_user(self, http_request:HttpRequest) -> HttpResponse:
        user_controller = UserController()

        body = http_request.body

        result = user_controller.create(body)

        return HttpResponse(status_code=201, body=result)
