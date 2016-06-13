import os
from playhouse.migrate import *
from flask_peewee.db import SqliteDatabase


from hello import app

db = SqliteDatabase('example.db')
migrator = SqliteMigrator(db)

weight = IntegerField(default=8000)
referenceNumber = TextField(default="123481")

migrate(
    migrator.add_column('load', 'weight', weight),
    migrator.add_column('load', 'referenceNumber', referenceNumber),
)
