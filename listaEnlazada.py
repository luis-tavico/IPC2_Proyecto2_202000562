class Nodo:
    def __init__(self, dato=None):
        self.dato = dato

class listaEnlazada:
    def __init__(self):
        self.primero = None
    
    def insertar(self, dato):
        if self.primero == None:
            self.primero = dato
            return
        actual = self.primero
        