from hello import db
import datetime
from peewee import TextField
from playhouse.postgres_ext import BinaryJSONField

class Result(db.Model):
    url = TextField()
    resukt_all = BinaryJSONField(default=lambda: {})
    resukt_no_stop_words =  BinaryJSONField(default=lambda: {})
