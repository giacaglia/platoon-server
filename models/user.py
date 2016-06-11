import datetime
from peewee import *
from peewee import *
from flask_peewee.db import SqliteDatabase
db = SqliteDatabase('example.db')

class User(Model):
    firstName = TextField()
    lastName = TextField()
    phoneNumber = TextField()
    truckType = TextField()
    plateNumber = TextField()
    image = TextField()

    class Meta:
        database = db
