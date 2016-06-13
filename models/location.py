import datetime
from peewee import *
from peewee import *
from flask_peewee.db import SqliteDatabase
db = SqliteDatabase('example.db')

class Location(Model):
    streetAddress = TextField()
    city = TextField()
    state = TextField()
    latitude = FloatField()
    longitude = FloatField()
    class Meta:
        database = db
