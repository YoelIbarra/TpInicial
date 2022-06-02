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

#Para porbar que anda el insert.
#insert_product('asd2','asd2','asda3e')

def select_products():
    results = Product.select()
    return results
def select_product_id(id):
    result = Product.select().where(Product.id == id).get()
    return result
"""
Prueba de select de productos
product = select_product_id(1)
print(product.type)

for fila in select_products():
    print(fila.type)
"""

"""
Prueba de update

"""