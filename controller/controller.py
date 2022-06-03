
from view.view import View
from model.model import Product


class Controller():

    def __init__(self):
        self.view = View(self)
        self.model = Product()

    def show_view(self):
        self.view.show_view()

    def get_registers(self):
        return self.model.get_products()

    def insert_product(self, product):
        return self.model.insert_product(product)

    def delete_product(self, product_id):
        self.model.delete_product(product_id)

    def update_product(self, product):
        self.model.update_product(product)
