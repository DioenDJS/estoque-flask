from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:


    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body.get("product_code")
        print("passando pela view")
        return HttpResponse(status_code=int(201), body=product_code)
