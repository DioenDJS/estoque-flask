from peewee import Model, CharField, IntegerField, AutoField, IntegrityError, ManyToManyField, ForeignKeyField, BooleanField
from playhouse.postgres_ext import UUIDField
from src.database.database import get_connect
from typing import Union, Type
from enum import Enum
import bcrypt
import uuid

db = get_connect()


class UserRoleEnum(Enum):
    ADMIN = 'ADMIN'
    CLIENT = 'CLIENT'
    PROVIDER = 'PROVIDER'
    SELLER = 'SELLER'
    USER = 'USER'

    @classmethod
    def get(cls: Type['UserRoleEnum'], value: Union[str, 'UserRoleEnum']) -> 'UserRoleEnum':
        if isinstance(value, cls):
            return value
        return cls[value]


class DepartmentEnum(Enum):
    MANAGER = 'MANAGER'
    STOCKIST = 'STOCKIST'
    SELLERS = 'SELLERS'

    @classmethod
    def get(cls: Type['DepartmentEnum'], value: Union[str, 'DepartmentEnum']) -> 'DepartmentEnum':
        if isinstance(value, cls):
            return value
        return cls[value]


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

    @classmethod
    def create_roles(cls):
        with db.atomic():
            try:
                for role_enum in UserRoleEnum:
                    cls.get_or_create(nome=role_enum.value)
            except IntegrityError as e:
                print(f"Erro ao criar roles: {e}")

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
    verification_code = IntegerField(null=True)
    validate_access = BooleanField(null=False, default=True)
    roles = ManyToManyField(Roles, backref='users', on_delete='CASCADE')

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


class Departments(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)

    @classmethod
    def create_departments(cls):
        with db.atomic():
            try:
                for departmen_enum in DepartmentEnum:
                    cls.get_or_create(name=departmen_enum.value)
            except IntegrityError as e:
                print(f"Erro ao criar Departments: {e}")

    def serialize(self):
        return {
            'id': str(self.id),
            'name': self.name
        }


class Employees(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    user = ForeignKeyField(Users, backref='employees', column_name='user_id', lazy_load=True, on_delete='CASCADE')
    department = ForeignKeyField(Departments, backref='employees', column_name='department_id', lazy_load=True)
    salary = IntegerField(null=False)

    def serialize(self):
        return {
            'id': str(self.id),
            'user_id': self.user.serialize(),
            'departament_id': self.department.serialize(),
            'salary': self.salary,
        }


def create_initial_roles():
    Roles.create_roles()


def create_initial_departments():
    Departments.create_departments()


def create_admin_user():
    admin_role = Roles.get(Roles.nome == UserRoleEnum.ADMIN.value)

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


db.create_tables([Products, Departments, Employees, Users, Roles, Users.roles.get_through_model()], safe=True)

create_initial_roles()
create_initial_departments()
create_admin_user()
