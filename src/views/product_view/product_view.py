from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.product.product_creator_controller import ProductCreatorController
from src.controllers.product.product_get_controller import ProductGetController


class ProductView:

    def validate_and_create_product(self, http_request: HttpRequest) -> HttpResponse:
        product_creator_controller = ProductCreatorController()
        body = http_request.body

        result = product_creator_controller.create(body)

        return HttpResponse(status_code=201, body=result)



    def find_all_product(self) -> HttpResponse:
        product_get_controller = ProductGetController()

        result = product_get_controller.get_all()

        return HttpResponse(status_code=200, body=result)