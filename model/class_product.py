from model.base_model import *

class Product(BaseModel):
    id = AutoField()
    type = CharField()
    model = CharField()
    reference = CharField()
    #insert = DateTimeField()

    def get_products():
        results = Product.select()
        return results

    def get_product_id(id):
        result = Product.select().where(Product.id == id).get()
        return result

    def insert_product(p_type,p_model,p_reference):
        product = Product()
        product.type = p_type
        product.model = p_model
        product.reference = p_reference
        #product.insert = date.datetime.now()

        product.save()

    def update_product(id, p_type, p_model, p_reference):
        product = Product.get_product_id(id)
        if (p_type != ""):
            product.type = p_type
        if (p_model != ""):
            product.model = p_model
        if (p_reference != ""):
            product.reference = p_reference
        product.save()

    def delete_product(id):
        product = Product.get_product_id(id)
        product.delete_instance()