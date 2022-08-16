from view.view import View
from model.class_product import Product
import model.db_config
from model.observer import ConcreteObserverA



class Controller():

    productos = []

    def __init__(self):
        """self.model = Product()"""
        self.view = View(self)

    def show_view(self):
        self.view.show_view()

    def get_registers(self):
        for p in Product.get_products():
            self.productos.append(p)
            ConcreteObserverA(p)
        return Product.get_products()

    def insert_product(self, tipo, modelo, referencia):
        p = Product.insert_product(tipo, modelo, referencia)
        self.productos.append(p)

    def delete_product(self, product_id):
        p = Product.get_product_id(product_id)
        self.productos.remove(p)
        Product.delete_product(product_id)

    def update_product(self, product_id, tipo, modelo, referencia):
        p = Product.update_product(product_id, tipo, modelo, referencia)
        self.productos.append(p)