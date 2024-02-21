from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField, BitField
from playhouse.postgres_ext import UUIDField
import bcrypt
from src.database.database import get_connect
import uuid

db = get_connect()

class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):

    id = CharField(primary_key=True, default=str(uuid.uuid4()))
    name = CharField()
    price = IntegerField()
    description = CharField()
    tag = CharField()


    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'tag': self.tag
        }

class User(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = CharField(null=False)
    email = CharField(unique=True, null=False)
    cpf = CharField(unique=True, null=False)
    smartphone = CharField(unique=True, null=False)
    password = CharField(null=False)

    def __hash_password(self, raw_password) -> bytes:
        return bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    def set_password(self, raw_password):
        self.password = self.__hash_password(raw_password)

    def check_password(self, raw_password) -> bytes:
        return bcrypt.checkpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    def serialize(self):
        return {
            'id': str(self.id),
            'full_name': self.full_name,
            'email': self.email,
            'cpf': self.cpf,
            'smartphone': self.smartphone,
            'password': self.password,
        }

class Employee(BaseModel):
        id = UUIDField(primary_key=True, default=uuid.uuid4)
        user = ForeignKeyField(User, backref='employee', column_name='user_id', lazy_load=True)
        departament = CharField(unique=True, null=False)
        salary = IntegerField(null=False)

        def serialize(self):
            return {
                'id': str(self.id),
                'user_id': self.user.serialize(),
                'departament': self.departament,
                'salary': self.salary,
            }


db.create_tables([Product, User, Employee], safe=True)
