from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.product_creator_controller import ProductCreatorController


class ProductCreatorView:

    def validate_and_create_product(self, http_request: HttpRequest) -> HttpResponse:
        product_creator_controller = ProductCreatorController()
        body = http_request.body
        print(body)

        result = product_creator_controller.create(body)

        print(f"O Resp e {type(result)}")
        return HttpResponse(status_code=201, body=result)
