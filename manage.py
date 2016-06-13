import os
from playhouse.migrate import *
from flask_peewee.db import SqliteDatabase


from hello import app

db = SqliteDatabase('example.db')
migrator = SqliteMigrator(db)

pallet_length = IntegerField(default=40)
pallet_width = IntegerField(default=48)
pallet_height = IntegerField(default=48)

migrate(
    migrator.add_column('load', 'pallet_length', pallet_length),
    migrator.add_column('load', 'pallet_width', pallet_width),
    migrator.add_column('load', 'pallet_height', pallet_height),
)
