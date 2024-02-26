from src.main.domain.models.models import Products
from src.database.database import get_connect
from typing import Dict


class ProductController:

    def create(self, product: dict) -> Dict:
        try:
            db = get_connect()
            new_product = Products.create(
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


    @staticmethod
    def get_all() -> Dict:

        try:
            with get_connect():
                products = Products.select()
                print(products)
                return {
                    "products": [{**product.serialize(), "price": "{:.2f}".format(product.price / 1000)} for product in products]
                }
        except Exception as e:
            print(f"Error: {e}")
            return {}