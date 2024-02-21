from src.database.database import get_connect
from src.main.domain.models.models import Product
from typing import Dict


def __formatted_list_in_dict(param):
    pass


class ProductGetController:


    @staticmethod
    def get_all() -> Dict:

        try:
            with get_connect():
                products = Product.select()
                print(products)
                return {
                    "products": [{**product.serialize(), "price": "{:.2f}".format(product.price / 1000)} for product in products]
                }
        except Exception as e:
            print(f"Error: {e}")
            return {}



