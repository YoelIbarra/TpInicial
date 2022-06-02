
from view.view import View
# from model.model import Model
# from tkinter import Tk


class Controller():

    def __init__(self):
        self.view = View(self)
        # self.model = Model()

    def show_view(self):
        self.view.show_view()
