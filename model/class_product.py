from model.base_model import BaseModel
from peewee import AutoField
from peewee import CharField
from peewee import DateTimeField


class Product(BaseModel):
    id = AutoField()
    type = CharField()
    model = CharField()
    reference = CharField()
    insert = DateTimeField()

    @staticmethod
    def get_products():
        results = Product.select()
        return results

    @staticmethod
    def get_product_id(id):
        result = Product.select().where(Product.id == id).get()
        return result

    @staticmethod
    def insert_product(p_type, p_model, p_reference, p_date):
        product = Product()
        product.type = p_type
        product.model = p_model
        product.reference = p_reference
        product.insert = p_date
        product.save()
        return product.id

    @staticmethod
    def update_product(id, p_type, p_model, p_reference):
        product = Product.get_product_id(id)
        if (p_type != ""):
            product.type = p_type
        if (p_model != ""):
            product.model = p_model
        if (p_reference != ""):
            product.reference = p_reference
        product.save()

    @staticmethod
    def delete_product(id):
        product = Product.get_product_id(id)
        product.delete_instance()
