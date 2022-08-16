import logging
logging.basicConfig(filename='controller.log',level="DEBUG")

class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        self.observadores.remove(obj)

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observado_a = obj
        self.observado_a.agregar(self)

    def update(self, *args):
        if(args[0]==0):
            logging.info("Insert")
        elif(args[0]==1):
            logging.info("Update")
        elif(args[0]==2):
            logging.info("Delete")
        else:
            logging.error("Acción no reconocida")