import xml.etree.ElementTree as ET
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloEscritorio import Escritorio
from modeloTransaccion import Transaccion
from modeloCliente import Cliente

class CargarArchivo:

    def leerArchivoConfiguracionSistema(self, ruta, listaEmpresas): 
        archivo_xml = ET.parse(ruta)
        empresas = archivo_xml.getroot()
  
        for empresa in empresas:
            listaPuntosAtencion = listaEnlazada()
            listaTransacciones = listaEnlazada()
            idEmpresa = empresa.attrib['id']
            nombreEmpresa = empresa.find('nombre').text
            abreviaturaEmpresa = empresa.find('abreviatura').text
            for puntosDeAtencion in empresa.findall('listaPuntosAtencion'):
                for puntoDeAtencion in puntosDeAtencion:
                    idPuntoAtencion = puntoDeAtencion.attrib['id']
                    nombrePuntoServicio = puntoDeAtencion.find('nombre').text
                    direccionPuntoServicio = puntoDeAtencion.find('direccion').text
                    for escritorios in puntoDeAtencion.findall('listaEscritorios'):
                        listaEscritorios = listaEnlazada()
                        for escritorio in escritorios:
                            idEscritorio = escritorio.attrib['id']
                            identificacion = escritorio.find('identificacion').text
                            nombreEncargado = escritorio.find('encargado').text
                            nuevoEscritorio = Escritorio(idEscritorio, identificacion, nombreEncargado, False)
                            listaEscritorios.insertar(nuevoEscritorio)
                    nuevoPuntoAtencion = PuntoAtencion(idPuntoAtencion, nombrePuntoServicio, direccionPuntoServicio, listaEscritorios)
                    listaPuntosAtencion.insertar(nuevoPuntoAtencion)
            for transacciones in empresa.findall('listaTransacciones'):
                for transaccion in transacciones:
                    idTransaccion = transaccion.attrib['id']
                    nombreTransaccion = transaccion.find('nombre').text
                    tiempoAtencion = transaccion.find('tiempoAtencion').text
                    nuevaTransaccion = Transaccion(id=idTransaccion, nombre=nombreTransaccion, tiempo=tiempoAtencion)
                    listaTransacciones.insertar(nuevaTransaccion)
            nuevaEmpresa = Empresa(idEmpresa, nombreEmpresa, abreviaturaEmpresa, listaPuntosAtencion, listaTransacciones)
            listaEmpresas.insertar(nuevaEmpresa)

        '''empresaEnLista = listaEmpresas.valores()
        print(empresaEnLista.dato.getId())
        print(empresaEnLista.dato.getNombre())
        print(empresaEnLista.dato.getAbreviatura())
        puntosAtencionEnLista = empresaEnLista.dato.getPuntosDeAtencion().valores()
        while puntosAtencionEnLista != None:
            print(puntosAtencionEnLista.dato.getId())
            print(puntosAtencionEnLista.dato.getNombre())
            print(puntosAtencionEnLista.dato.getDireccion())
            escritoriosEnLista = puntosAtencionEnLista.dato.getEscritorios().valores()
            while escritoriosEnLista != None:
                print(escritoriosEnLista.dato.getId())
                print(escritoriosEnLista.dato.getIdentificacionEscritorio())
                print(escritoriosEnLista.dato.getNombreEncargado())
                print(escritoriosEnLista.dato.getEstado())
                escritoriosEnLista = escritoriosEnLista.siguiente
            puntosAtencionEnLista = puntosAtencionEnLista.siguiente
        transaccionesEnLista = empresaEnLista.dato.getTransacciones().valores()
        while transaccionesEnLista != None:
            print(transaccionesEnLista.dato.getId())
            print(transaccionesEnLista.dato.getNombre())
            print(transaccionesEnLista.dato.getTiempo())
            print(transaccionesEnLista.dato.getCantidad())
            transaccionesEnLista = transaccionesEnLista.siguiente'''        

    def leerArchivoConfiguracionInicial(self, ruta, listaEmpresas):
        archivo_xml = ET.parse(ruta)
        estadoInicial = archivo_xml.getroot()

        for configInicial in estadoInicial:
            id = configInicial.attrib['id']
            idEmpresa = configInicial.attrib['idEmpresa']      
            idPunto = configInicial.attrib['idPunto']
            empresa = listaEmpresas.buscarId(idEmpresa)
            listaPuntos = empresa.dato.getPuntosDeAtencion()
            punto = listaPuntos.buscarId(idPunto)
            listaEscritorios = punto.dato.getEscritorios()
            listaEscritoriosActivos = listaEnlazada()
            for escritoriosActivos in configInicial.findall('escritoriosActivos'):
                for escritorio in escritoriosActivos:
                    idEscritorio = escritorio.attrib['idEscritorio']
                    escritorio = listaEscritorios.buscarId(idEscritorio)
                    listaEscritoriosActivos.insertar(escritorio.dato)
                    escritorio.dato.setEstado(True)
            punto.dato.setEscritoriosActivos(listaEscritoriosActivos)
            listaClientes = listaEnlazada()
            for clientes in configInicial.findall('listadoClientes'):  
                for cliente in clientes:
                    punto.dato.setTurnoEnPunto()
                    dpiCliente = cliente.attrib['dpi']
                    nombreCliente = cliente.find('nombre').text
                    listaTransacciones = listaEnlazada()
                    for listadoTransacciones in cliente.findall('listadoTransacciones'):
                        for transaccion in listadoTransacciones:
                            idTransaccion = transaccion.attrib['idTransaccion']
                            cantidad = transaccion.attrib['cantidad']
                            nuevaTransaccion = Transaccion(id=idTransaccion, cantidad=cantidad)
                            listaTransacciones.insertar(nuevaTransaccion)
                    nuevoCliente = Cliente(dpiCliente, nombreCliente, listaTransacciones)
                    listaClientes.insertar(nuevoCliente)
                    punto.dato.setClientes(listaClientes)



        '''clientesEnLista = listaClientes.valores()
        print(clientesEnLista.dato.getId())
        print(clientesEnLista.dato.getNombre())'''

        '''empresaEnLista = listaEmpresas.valores()
        print(empresaEnLista.dato.getId())
        print(empresaEnLista.dato.getNombre())
        print(empresaEnLista.dato.getAbreviatura())
        puntosAtencionEnLista = empresaEnLista.dato.getPuntosDeAtencion().valores()
        while puntosAtencionEnLista != None:
            print(puntosAtencionEnLista.dato.getId())
            print(puntosAtencionEnLista.dato.getNombre())
            print(puntosAtencionEnLista.dato.getDireccion())
            escritoriosEnLista = puntosAtencionEnLista.dato.getEscritorios().valores()
            while escritoriosEnLista != None:
                print(escritoriosEnLista.dato.getId())
                print(escritoriosEnLista.dato.getIdentificacionEscritorio())
                print(escritoriosEnLista.dato.getNombreEncargado())
                print(escritoriosEnLista.dato.getEstado())
                escritoriosEnLista = escritoriosEnLista.siguiente
            puntosAtencionEnLista = puntosAtencionEnLista.siguiente
        transaccionesEnLista = empresaEnLista.dato.getTransacciones().valores()
        while transaccionesEnLista != None:
            print(transaccionesEnLista.dato.getId())
            print(transaccionesEnLista.dato.getNombre())
            print(transaccionesEnLista.dato.getTiempo())
            print(transaccionesEnLista.dato.getCantidad())
            transaccionesEnLista = transaccionesEnLista.siguiente''' 

'''listaEmpresas = listaEnlazada()
archivo = CargarArchivo()
archivo.leerArchivoConfiguracionSistema("ConfiguracionSistema2.xml", listaEmpresas)
print("-----------")
archivo.leerArchivoConfiguracionInicial("ConfiguracionInicial2.xml", listaEmpresas)'''