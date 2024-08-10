from typing import Dict
from src.database.database import get_connect
from src.main.domain.models.models import Address


class AddressController:

    def create(self, adrress: dict) ->Dict:
        db = get_connect()
        new_address = Address.create(
            street=adrress.get("street"),
            city=adrress.get("city"),
            state=adrress.get("state"),
            number=adrress.get("number"),
            zip_code=adrress.get("zip_code"),
            complement=adrress.get("complement"),
            Neighborhood=adrress.get("Neighborhood")
        )
        new_address.save()
        return {
            "data": {
                "id": new_address.id
            }
        }
