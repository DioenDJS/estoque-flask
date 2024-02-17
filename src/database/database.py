import peewee
from dotenv import load_dotenv
import os


def get_connect():
    load_dotenv()
    db = peewee.PostgresqlDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT_DOCKER"))
    return db


def create_table(table):
    db = get_connect()
    db.connect()
    db.create_tables([table], safe=True)
