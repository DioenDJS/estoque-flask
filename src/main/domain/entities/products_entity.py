from src.database.database import create_table, get_connect
from peewee import Model, CharField, DecimalField
import uuid


class Product(Model):

    id = CharField(primary_key=True, default=str(uuid.uuid4()))
    name = CharField()
    price = DecimalField()
    description = CharField()
    tag = CharField()

    class Meta:
        database = get_connect()


create_table(Product)
