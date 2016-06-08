import datetime
from peewee import *
from flask_peewee.db import SqliteDatabase
db = SqliteDatabase('example.db')

class Company(Model):
    name = TextField()
    rating = FloatField()

    class Meta:
        database = db
