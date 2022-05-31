from peewee import *

database = SqliteDatabase('prueba.db')

class BaseModel(Model):
    class Meta:
        database = database

class Product(BaseModel):
    id = AutoField()
    type = CharField()
    model = CharField()
    reference = CharField()
    insert = DateField()


database.connect()
database.create_tables([Product])