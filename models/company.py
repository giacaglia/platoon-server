from hello import db
import datetime
from peewee import *

db = SqliteDatabase('example.db')
class Company(Model):
    name = TextField()
    rating = FloatField()

    class Meta:
        database = db
