from peewee import Model, CharField, IntegerField, AutoField, IntegrityError, ManyToManyField
from playhouse.postgres_ext import UUIDField
from src.database.database import get_connect
import bcrypt
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
    roles = ManyToManyField(Roles, backref='users')

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
            'roles': [role.serialize() for role in self.roles],
        }


def create_initial_roles(roles_data):
    with db.atomic():
        try:
            for role_name in roles_data:
                Roles.get_or_create(nome=role_name)
        except IntegrityError:
            pass


def create_admin_user():
    admin_role = Roles.get(Roles.nome == 'ADMIN')

    with db.atomic():
        try:
            admin_user = Users.create(
                full_name='Admin User',
                email='admin@example.com',
                cpf='12345678900',
                smartphone='123456789',
                password='admin_password'
            )
            admin_user.set_password('admin_password')
            admin_user.roles.add(admin_role)
            admin_user.save()
        except IntegrityError:
            pass

db.create_tables([Products, Users, Roles, Users.roles.get_through_model()], safe=True)


roles_to_seed = ['ADMIN', 'PROVIDER', 'SELLER', 'CLIENT']
create_initial_roles(roles_to_seed)
create_admin_user()
