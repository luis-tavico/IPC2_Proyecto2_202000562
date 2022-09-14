class Transaccion:

    def __init__(self, id, nombre, tiempo):
        self.id = id
        self.nombre = nombre
        self.tiempo = tiempo

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getTiempo(self):
        return self.tiempo

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTiempo(self, tiempo):
        self.tiempo = tiempo