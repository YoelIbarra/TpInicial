
from view.view import View
from model.model import Product


class Controller():

    def __init__(self):
        self.view = View(self)
        self.model = Product()

    def show_view(self):
        self.view.show_view()
