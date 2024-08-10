from peewee import Model, CharField, IntegerField, AutoField, IntegrityError, ManyToManyField, ForeignKeyField, DateField, DateTimeField, SQL
from datetime import datetime, timedelta
from playhouse.postgres_ext import UUIDField
from src.database.database import get_connect
from typing import Union, Type
from src.main.domain.enums.AccessStatus import AccessStatusEnum
from enum import Enum
import bcrypt
import uuid
import pytz
import os

# Defina o fuso horário desejado
os.environ['TZ'] = 'America/Sao_Paulo'

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
    created_at = DateTimeField(default=datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)

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
    created_at = DateTimeField(default=datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)

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


class Address(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    street = CharField()
    city = CharField()
    state = CharField()
    number = IntegerField()
    zip_code = CharField()
    complement = CharField()
    Neighborhood = CharField()

    def serialize(self):
        return {
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'number': self.number,
            'zip_code': self.zip_code,
            'complement': self.complement,
            'Neighborhood': self.Neighborhood
        }


class Users(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = CharField(null=False)
    email = CharField(unique=True, null=False)
    cpf = CharField(unique=True, null=True)
    birthday = DateField(null=True)
    smartphone = CharField(unique=True, null=False)
    password = CharField(null=False)
    verification_code = IntegerField(null=True)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)
    validate_access = CharField(null=False, default=AccessStatusEnum.ACTIVE.value)
    roles = ManyToManyField(Roles, backref='users', on_delete='CASCADE')
    address = ForeignKeyField(Address, backref='users', null=True, on_delete='CASCADE')


    def __hash_password(self, raw_password) -> bytes:
        return bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

    def set_password(self, raw_password):
        self.password = self.__hash_password(raw_password)

    def check_password(self, raw_password) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

    def serialize(self):
        return {
            'id': str(self.id),
            'full_name': self.full_name,
            'email': self.email,
            'cpf': self.cpf,
            'birthday': self.birthday.isoformat() if self.birthday else None,
            'smartphone': self.smartphone,
            'password': self.password,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
            'validate_access': self.validate_access,
            'roles': [role.serialize() for role in self.roles],
            'address': self.address.serialize()
        }


class FinalUsersPhysicalPerson(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    user = ForeignKeyField(Users, backref='finalusersphysicalperson', column_name='user', lazy_load=True, on_delete='CASCADE')

    def serialize(self):
        return {
            'id': str(self.id),
            'user': self.user.serialize()
        }


class Departments(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(unique=True)
    created_at = DateTimeField(default=datetime.now(pytz.timezone('America/Sao_Paulo')))
    updated_at = DateTimeField(null=True)
    deleted_at = DateTimeField(null=True)

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


db.create_tables([Products, Departments, Employees, Users, Roles, Address, FinalUsersPhysicalPerson, Users.roles.get_through_model()], safe=True)

create_initial_roles()
create_initial_departments()
create_admin_user()
