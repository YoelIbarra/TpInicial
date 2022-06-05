from peewee import SqliteDatabase
from model.class_product import Product

database = SqliteDatabase('prueba.db')

database.connect()
lista_tablas = []

if not(database.table_exists(Product)):
    lista_tablas.append(Product)

if (lista_tablas != []):
    database.create_tables(lista_tablas)
