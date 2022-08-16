from view.view import View
from model.class_product import Product
import model.db_config
import logging


class Controller():

    logging.basicConfig(filename='controller.log',level="DEBUG")

    def __init__(self):
        self.model = Product()
        self.view = View(self)

    def show_view(self):
        self.view.show_view()

    def get_registers(self):
        return self.model.get_products()

    def insert_product(self, tipo, modelo, referencia):
        """
        Ejemplo de uso de lo que es el Logging, esto se deberá hacer desde el archivo observer.py que esta dentro de los modelos. Ahí esta explicada la idea.
        try:
            self.model.insert_product(tipo, modelo, referencia)
            logging.info("Se inserto el producto de tipo %s y modelo %s",tipo,modelo)
        except:
            logging.error("no se inserto nada")
        """
        self.model.insert_product(tipo, modelo, referencia)

    def delete_product(self, product_id):
        self.model.delete_product(product_id)

    def update_product(self, product_id, tipo, modelo, referencia):
        self.model.update_product(product_id, tipo, modelo, referencia)
