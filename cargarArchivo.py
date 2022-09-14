import xml.etree.ElementTree as ET

class CargarArchivo:

    def leerArchivoConfiguracionSistema(self, ruta): 
        archivo_xml = ET.parse(ruta)
        empresas = archivo_xml.getroot()

        for empresa in empresas:
            nombreEmpresa = empresa.find('nombre').text
            abreviaturaEmpresa = empresa.find('abreviatura').text
            for puntosDeAtencion in empresa.findall('listaPuntosAtencion'):
                for puntoDeAtencion in puntosDeAtencion:
                    nombrePuntoServicio = puntoDeAtencion.find('nombre').text
                    direccionPuntoServicio = puntoDeAtencion.find('direccion').text
                    for listaEscritorios in puntoDeAtencion.findall('listaEscritorios'):
                        for escritorio in listaEscritorios:
                            identificacion = escritorio.find('identificacion').text
                            encargado = escritorio.find('encargado').text
            for listaTransacciones in empresa.findall('listaTransacciones'):
                for transaccion in listaTransacciones:
                    nombreTransaccion = transaccion.find('nombre').text
                    tiempoAtencion = transaccion.find('tiempoAtencion').text

    def leerArchivoConfiguracionInicial(self, ruta):
        archivo_xml = ET.parse(ruta)
        estadoInicial = archivo_xml.getroot()

        for configInicial in estadoInicial:
            for escritoriosActivos in configInicial.findall('escritoriosActivos'):
                for escritorio in escritoriosActivos:
                    idEscritorio = escritorio.attrib['idEscritorio']
                    print(idEscritorio)
            for listadoClientes in configInicial.findall('listadoClientes'):  
                for cliente in listadoClientes:
                    nombreCliente = cliente.find('nombre').text
                    for listadoTransacciones in cliente.findall('listadoTransacciones'):
                        for transaccion in listadoTransacciones:
                            idTransaccion = transaccion.attrib['idTransaccion']
                            cantidad = transaccion.attrib['cantidad']