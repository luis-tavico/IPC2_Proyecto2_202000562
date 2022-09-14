class Empresa:

    def __init__(self, id, nombre, abreviatura):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getAbreviatura(self):
        return self.abreviatura

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setAbreviatura(self, abreviatura):
        self.abreviatura = abreviatura