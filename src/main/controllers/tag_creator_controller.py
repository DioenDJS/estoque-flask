from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler


class CreateTagController:

    def __init__(self, barcode_handler: BarcodeHandler):
        self.barcode_handler = barcode_handler

    def create(self, product_code: str) -> Dict[str, Dict[str, int]]:
        path_from_tag = self.__create_tag(product_code)
        formatter_response = self.__format_response(path_from_tag)
         return formatter_response


    def __create_tag(self, product_code: str) -> str:
        path_from_tag = self.barcode_handler.create.barcode(product_code)
        return path_from_tag


    def __format_response(self, path_from_tag: str) -> Dict[str, Dict[str, int]]:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
