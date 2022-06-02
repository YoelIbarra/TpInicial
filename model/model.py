from math import prod
from peewee import *
import datetime as date

database = SqliteDatabase('prueba.db')

class BaseModel(Model):
    class Meta:
        database = database

class Product(BaseModel):
    id = AutoField()
    type = CharField()
    model = CharField()
    reference = CharField()
    #insert = DateTimeField()


database.connect()
database.create_tables([Product])

def insert_product(p_type,p_model,p_reference):
    product = Product()
    product.type = p_type
    product.model = p_model
    product.reference = p_reference
    #product.insert = date.datetime.now()

    product.save()

insert_product('asd','asd2','asda3e')