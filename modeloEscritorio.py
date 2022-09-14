class Escritorio:

    def __init__(self, id, identificacionEscritorio, nombreEncargado):
        self.id = id
        self.identificacionEscritorio = identificacionEscritorio
        self.nombreEncargado = nombreEncargado

    def getId(self):
        return self.id

    def getIdentificacionEscritorio(self):
        return self.identificacionEscritorio

    def getNombreEncargado(self):
        return self.nombreEncargado

    def setId(self, id):
        self.id = id

    def setIdentificacionEscritorio(self, identificacionEscritorio):
        self.identificacionEscritorio = identificacionEscritorio

    def setNombreEncargado(self, nombreEncargado):
        self.nombreEncargado = nombreEncargado