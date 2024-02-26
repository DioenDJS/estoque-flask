from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.product.product_controller import ProductController


class ProductView:

    def validate_and_create_product(self, http_request: HttpRequest) -> HttpResponse:
        product_creator_controller = ProductController()
        body = http_request.body

        result = product_creator_controller.create(body)

        return HttpResponse(status_code=201, body=result)



    def find_all_product(self) -> HttpResponse:
        product_get_controller = ProductController()

        result = product_get_controller.get_all()

        return HttpResponse(status_code=200, body=result)
