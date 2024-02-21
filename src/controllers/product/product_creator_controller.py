# from src.main.domain.models.products_entity import Product
from src.main.domain.models.models import Product
from src.database.database import get_connect
from typing import Dict


class ProductCreatorController:

    def create(self, product: dict) -> Dict:
        try:
            db = get_connect()
            new_product = Product.create(
                name=product.get('name'),
                price=int(product.get('price') * 1000),
                description=product.get('description'),
                tag=product.get('tag')
            )

            id = new_product.id
            new_product.save()
            return self.__format(id)
        except Exception as e:
            print(f"o erro {str(e)}")

    def __format(self, id_created_product: str) -> Dict:
        return {
            "data": {
                "id": id_created_product
            }
        }
