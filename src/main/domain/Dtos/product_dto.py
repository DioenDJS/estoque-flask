from typing import Optional


class ProductDTO:
    def __init__(self, name: str, price: float, description: Optional[str] = None, tag: Optional[str] = None):
        self.name = name
        self.price = price
        self.description = description
        self.tag = tag
