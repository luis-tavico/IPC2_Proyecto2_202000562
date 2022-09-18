class PuntoAtencion:
    
    def __init__(self, id, nombre, direccion, escritorios, clientes=None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.escritorios = escritorios
        self.clientes = clientes

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getEscritorios(self):
        return self.escritorios

    def getClientes(self):
        return self.clientes

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setDireccion(self, direccion):
        self.direccion = direccion
    
    def setEscritorios(self, escritorios):
        self.escritorios = escritorios

    def setClientes(self, clientes):
        self.clientes = clientes