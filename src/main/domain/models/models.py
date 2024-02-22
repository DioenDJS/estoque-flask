from peewee import Model, CharField, IntegerField, ForeignKeyField, AutoField
from playhouse.postgres_ext import UUIDField
import bcrypt
from src.database.database import get_connect
from playhouse.migrate import *
import uuid

db = get_connect()


class BaseModel(Model):
    class Meta:
        database = db


class Products(BaseModel):

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

class Roles(BaseModel):
    id = AutoField(primary_key=True)
    nome = CharField(unique=True)

    def serialize(self):
        return {
            'id': str(self.id),
            'nome': self.nome
        }

class Users(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = CharField(null=False)
    email = CharField(unique=True, null=False)
    cpf = CharField(unique=True, null=False)
    smartphone = CharField(unique=True, null=False)
    password = CharField(null=False)
    role = ForeignKeyField(Roles, backref='user', column_name='role_id', lazy_load=True)

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
            'role': self.role.serialize() if self.role else None
        }


class UsersRoles(BaseModel):
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(Users, backref='usersroles', column_name='user_id', on_delete='CASCADE')
    role_id = ForeignKeyField(Roles, backref='usersroles', column_name='role_id', on_delete='CASCADE')


class Employees(BaseModel):
        id = UUIDField(primary_key=True, default=uuid.uuid4)
        user = ForeignKeyField(Users, backref='employee', column_name='user_id', lazy_load=True, on_delete='CASCADE')
        departament = CharField(unique=True, null=False)
        salary = IntegerField(null=False)

        def serialize(self):
            return {
                'id': str(self.id),
                'user_id': self.user.serialize(),
                'departament': self.departament,
                'salary': self.salary,
            }





def create_initial_roles(roles_data):
    with db.atomic():
        try:
            for role_name in roles_data:
                Roles.create(nome=role_name)
        except IntegrityError:
            # Lidar com erro de integridade se as roles já existirem
            pass


db.create_tables([Products, Users, Employees, Roles, UsersRoles], safe=True)



# Inicializar as roles
roles_to_seed = ['ADMIN', 'PROVIDER', 'SELLER', 'CLIENT']
create_initial_roles(roles_to_seed)