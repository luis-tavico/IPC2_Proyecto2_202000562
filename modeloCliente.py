class Cliente:

    def __init__(self, dpi, nombre):
        self.dpi = dpi
        self.nombre = nombre

    def getDPI(self):
        return self.dpi

    def getNombre(self):
        return self.nombre

    def setDPI(self, dpi):
        self.dpi = dpi

    def setNombre(self, nombre):
        self.nombre = nombre