import peewee
from dotenv import load_dotenv
import os


def get_connect():
    load_dotenv()
    db = peewee.PostgresqlDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host="localhost", port=os.getenv("DB_PORT"))
    return db


