from model.base_model import BaseModel
from peewee import AutoField
from peewee import CharField
from model.observer import ConcreteObserverA
from model.observer import Sujeto

class Product(Sujeto, BaseModel):    

    id = AutoField()
    type = CharField()
    model = CharField()
    reference = CharField()


    @staticmethod
    def get_products():
        results = Product.select()
        return results

    @staticmethod
    def get_product_id(id):
        result = Product.select().where(Product.id == id).get()
        return result

    @staticmethod
    def insert_product(self, p_type, p_model, p_reference):
        product = Product()
        product.type = p_type
        product.model = p_model
        product.reference = p_reference
        product.save()
        self.notificar(0)
        return product

    @staticmethod
    def update_product(self, id, p_type, p_model, p_reference):
        product = Product.get_product_id(id)
        if (p_type != ""):
            product.type = p_type
        if (p_model != ""):
            product.model = p_model
        if (p_reference != ""):
            product.reference = p_reference
        product.save()
        self.notificar(1)
        return product

    @staticmethod
    def delete_product(self, id):
        product = Product.get_product_id(id)
        self.notificar(2)
        product.delete_instance()
        
