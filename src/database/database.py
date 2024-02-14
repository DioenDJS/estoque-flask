import peewee
from dotenv import load_dotenv
import os
# import psycopg2
#
#
# def get_connet_psycopg2():
#     conn = psycopg2.connect(dbname="estoque_flask", user="user_test")
#     return conn


def get_connect():
    load_dotenv()
    db = peewee.PostgresqlDatabase(os.getenv("DB_NAME"), user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    return db


def create_table(table):
    db = get_connect()
    db.connect()
    db.create_tables([table], safe=True)
