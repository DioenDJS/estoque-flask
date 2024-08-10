from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.final_user.final_user_controller import FinalUserController


class FinalUserView:
    final_user_controller = FinalUserController()

    def validate_and_create_final_users_physical_person(self, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        result = self.final_user_controller.create(body)

        return HttpResponse(status_code=201, body=result)


    def final_users_physical_person_update(self, id: str, http_request: HttpRequest) -> HttpResponse:

        body = http_request.body

        result = self.final_user_controller.update(id, body)

        return HttpResponse(status_code=201, body=result)


    def get_final_users(self) -> HttpResponse:


        result = self.final_user_controller.find_all()
        return HttpResponse(status_code=201, body=result)


    def get_final_users_by_id(self,http_request: HttpRequest) -> HttpResponse:

        final_user_id = http_request.query_params.get('final_user_id')

        result = self.final_user_controller.find_by_id(final_user_id)

        return HttpResponse(status_code=201, body=result)


    def delete_final_users(self,http_request: HttpRequest) -> HttpResponse:

        final_user_id = http_request.query_params.get('final_user_id')

        result = self.final_user_controller.soft_delete(final_user_id)

        return HttpResponse(status_code=201, body=result)
