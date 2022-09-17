class Cliente:

    def __init__(self, dpi, nombre, transacciones):
        self.dpi = dpi
        self.nombre = nombre
        self.transacciones = transacciones

    def getId(self):
        return self.dpi

    def getNombre(self):
        return self.nombre

    def getTransacciones(self):
        return self.transacciones

    def setId(self, dpi):
        self.dpi = dpi

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTransacciones(self, transacciones):
        self.transacciones = transacciones