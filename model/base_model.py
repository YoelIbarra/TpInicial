from peewee import Model
from peewee import SqliteDatabase


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('prueba.db')
