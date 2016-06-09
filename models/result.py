import datetime
from peewee import TextField, Model, SqliteDatabase
from playhouse.postgres_ext import JSONField

db = SqliteDatabase('example.db')
class Result(Model):
    url = TextField()
    result_all = TextField()
    # result_no_stop_words =  JSONField()

    class Meta:
        database = db
