from view.view import View
from model.class_product import Product
#
import model.db_config


class Controller():

    def __init__(self):
        self.model = Product()
        self.view = View(self)

    def show_view(self):
        self.view.show_view()

    def get_registers(self):
        return self.model.get_products()

    def insert_product(self, tipo, modelo, referencia):
        self.model.insert_product(tipo, modelo, referencia)

    def delete_product(self, product_id):
        self.model.delete_product(product_id)

    def update_product(self, product_id, tipo, modelo, referencia):
        self.model.update_product(product_id, tipo, modelo, referencia)
