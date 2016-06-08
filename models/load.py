from hello import db
import datetime
from peewee import *

db = SqliteDatabase('example.db')
class Load(Model):
    pickUp = TextField()
    dropOff = TextField()
    timePickUp = DateField()
    loadType = TextField()
    numberPallets = IntegerField()
    totalPrice = IntegerField()
    pricePerLoad = FloatField()

    class Meta:
        database = db
