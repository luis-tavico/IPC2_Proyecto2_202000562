class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class listaEnlazada:
    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    def insertar(self, dato):
        if self.primero is None:
            self.primero = Nodo(dato=dato)
            self.tamanio += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=dato)
        self.tamanio += 1

    def valores(self):
        valores = self.primero
        return valores

    def longitud(self):
        return self.tamanio

    def eliminar(self):
        actual = self.primero
        anterior = None
    
        while actual and actual.siguiente != None:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def buscar(self, id):
        actual = self.primero
        anterior = None

        while actual and actual.dato.getId() != id:
            anterior = actual
            actual = actual.siguiente
            
        if actual != None:
            return actual  
        else:
            return