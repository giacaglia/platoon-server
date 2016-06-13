import datetime
from peewee import *
from company import *
from flask_peewee.db import SqliteDatabase

db = SqliteDatabase('example.db')
class Load(Model):
    company = ForeignKeyField(Company, related_name='companies')
    pickUp = TextField()
    dropOff = TextField()
    timePickUp = DateField()
    loadType = TextField()
    numberPallets = IntegerField()
    totalPrice = IntegerField()
    pricePerLoad = FloatField()
    weight = IntegerField()
    referenceNumber = TextField()

    pallet_length = IntegerField()
    pallet_width = IntegerField()
    pallet_height = IntegerField()

    class Meta:
        database = db
