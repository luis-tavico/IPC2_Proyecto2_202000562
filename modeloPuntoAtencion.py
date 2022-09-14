class PuntoAtencion:
    
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion