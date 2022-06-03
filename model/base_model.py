from math import prod
from peewee import *
import datetime as date


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('prueba.db')

#Para porbar que anda el insert.
#insert_product('asd2','asd2','asda3e')


"""
Prueba de select de productos
product = select_product_id(1)
print(product.type)

for fila in select_products():
    print(fila.type)
"""


"""
Prueba de update

print(select_product_id(1).type)
update_product(1,"modificado","ads","ads")
print(select_product_id(1).type)
"""


"""
Prueba delete

print(select_product_id(1).type)
delete_product(1)
try:
    if(select_product_id(1)):
        print("esta")
except:
    print("no esta")   

    """