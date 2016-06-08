from hello import db
import datetime
from peewee import *

db = SqliteDatabase('example.db')
class User(Model):
    firstName = TextField()
    lastName = FloatField()
    phoneNumber = TextField()
    truckType = TextField()
    plateNumber = TextField()
    image = TextField()

    class Meta:
        database = db
