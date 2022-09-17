from cargarArchivo import CargarArchivo
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloEscritorio import Escritorio
from modeloTransaccion import Transaccion

class menuPrincipal:
    
    def __init__(self):
        self.listaEmpresas = listaEnlazada()
        self.menu()

    def menu(self):
        idEmpresa = 0
        while True:
            print(" -----------------Menu Principal----------------- ")
            print("| 1. Configuracion de Empresas                   |")
            print("| 2. Seleccion de Empresa y Punto de Atencion    |")
            print("| 3. Manejo de Puntos de Atencion                |")
            print("| 4. Limpiar Sistema                             |")
            print("| 5. Salir                                       |")
            print(" ------------------------------------------------ ")
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    menu = True
                    while menu:
                        print(" -----------Configuracion de Empresas------------ ")
                        print("| 1. Cargar Archivo de Configuracion del Sistema |")
                        print("| 2. Cargar Archivo con Configuracion Inicial    |")
                        print("| 3. Crear Nueva Empresa                         |")
                        print("| 4. Regresar al Menu Principal                  |")
                        print(" ------------------------------------------------ ")
                        try:
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                #ConfiguracionSistema.xml
                                ruta = input("Ingrese la ruta del archivo -> ")
                                archivo = CargarArchivo()
                                archivo.leerArchivoConfiguracionSistema(ruta, self.listaEmpresas)
                            elif opcion == 2:
                                #ConfiguracionInicial.xml
                                ruta = input("Ingrese la ruta del archivo -> ")
                                archivo = CargarArchivo()
                                archivo.leerArchivoConfiguracionInicial(ruta, self.listaEmpresas)         
                            elif opcion == 3:     
                                idPuntoAtencion = 0
                                idTransaccion = 0
                                print("------------Nueva Empresa-------------")
                                nombreEmpresa = input("Ingrese el nombre: ")
                                abreviatura = input("ingrese la abreviatura: ")
                                listaPuntosAtencion = listaEnlazada()
                                listaTransacciones = listaEnlazada()
                                while True:
                                    print(" --------------------Agregar--------------------- ")
                                    print("| 1. Punto de Atencion y Escritorios de Servicio |")
                                    print("| 2. Transacciones                               |")
                                    print("| 3. Regresar a Configuracion de Empresas        |")
                                    print("| 4. Regresar al Menu Principal                  |")
                                    print(" ------------------------------------------------ ")
                                    try:
                                        opcion = int(input("Ingrese una opcion: "))
                                        idEscritorio = 0
                                        if opcion == 1:                              
                                            print("-------Nuevo Punto de Atencion--------")
                                            idPuntoAtencion += 1 
                                            nombrePuntoAtencion = input("Ingrese el nombre: ")
                                            direccionPuntoAtencion = input("Ingrese la direccion: ")             
                                            listaEscritorio = listaEnlazada()
                                            while True:
                                                print("-----Nuevo Escritorio de Servicio-----")
                                                idEscritorio += 1
                                                identificacionEscritorio = input("Ingrese la identificacion del escritorio: ")
                                                nombreEncargado = input("Ingrese el nombre del encargado: ")
                                                escritorio = Escritorio(idEscritorio, identificacionEscritorio, nombreEncargado, True)
                                                listaEscritorio.insertar(escritorio)
                                                respuesta = input("¿Desea agregar otro escritorio? (s/n) ")
                                                if respuesta == 'n':
                                                    puntoAtencion = PuntoAtencion(idPuntoAtencion, nombrePuntoAtencion, direccionPuntoAtencion, listaEscritorio)
                                                    listaPuntosAtencion.insertar(puntoAtencion)
                                                    print("¡Punto de atencion y escritorio(s) agregados exitosamente!")
                                                    break                               
                                        elif opcion == 2:                                       
                                            while True:
                                                print("----------Nueva Transaccion-----------")
                                                idTransaccion += 1
                                                iden = input("Ingrese el nombre: ")
                                                nombre = input("Ingrese el nombre: ")             
                                                respuesta = input("¿Desea agregar otra transaccion? (s/n) ")
                                                transaccion = Transaccion(id=idTransaccion, nombre=nombre)
                                                listaTransacciones.insertar(transaccion)
                                                if respuesta == 'n':
                                                    print("¡Transaccion(es) agregada(s) exitosamente!")
                                                    break 
                                        elif opcion == 3:
                                            idEmpresa += 1
                                            empresa = Empresa(idEmpresa, nombreEmpresa, abreviatura, listaPuntosAtencion, listaTransacciones)
                                            self.listaEmpresas.insertar(empresa)
                                            break
                                        elif opcion == 4:
                                            idEmpresa += 1
                                            empresa = Empresa(idEmpresa, nombreEmpresa, abreviatura, listaPuntosAtencion, listaTransacciones)
                                            self.listaEmpresas.insertar(empresa)
                                            menu = False
                                            break
                                        else: 
                                            print("¡Ingrese una opcion valida!")
                                    except ValueError:
                                        print("¡Ingrese solo numeros!")
                            elif opcion == 4:
                                break
                            else: 
                                print("¡Ingrese una opcion valida!")
                        except ValueError:
                            print("¡Ingrese solo numeros!")
                        except FileNotFoundError:
                            print("¡El archivo no existe!")                     
                elif opcion == 2:
                    #ConfiguracionSistema2.xml
                    #ConfiguracionInicial2.xml
                    if self.listaEmpresas.valores() != None:
                        empresaEnLista = self.listaEmpresas.valores()
                        print(" ----------------------------------- ")
                        print("|     Id     |        Nombre        |")
                        print("|-----------------------------------|")
                        while empresaEnLista != None:
                            print("|", empresaEnLista.dato.getId(), (9-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(), (19-len(empresaEnLista.dato.getNombre()))*(" "), ("|"))
                            empresaEnLista = empresaEnLista.siguiente
                        print(" ----------------------------------- ")
                        idEmpresa = input("Ingrese el id de la empresa: ")            
                        empresa = self.listaEmpresas.buscar(idEmpresa)
                        if empresa != None:
                            listaPuntosAtencion = empresa.dato.getPuntosDeAtencion().valores()
                            print(" --------------------------------------------------------- ")
                            print("|     Id     |        Nombre        |      Direccion      |")
                            print("|---------------------------------------------------------|")
                            while listaPuntosAtencion != None:
                                print("|", listaPuntosAtencion.dato.getId(), (9-len(str(listaPuntosAtencion.dato.getId())))*(" "), "|", listaPuntosAtencion.dato.getNombre(), (19-len(listaPuntosAtencion.dato.getNombre()))*(" "), "|", listaPuntosAtencion.dato.getDireccion(), (18-len(listaPuntosAtencion.dato.getDireccion()))*(" "), ("|"))
                                listaPuntosAtencion = listaPuntosAtencion.siguiente
                            print(" --------------------------------------------------------- ")
                            idPunto = input("Ingrese el id del punto de atencion: ")  
                            listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()
                            if idPunto != None:    
                                punto = listaPuntosAtencion.buscar(idPunto)
                                listaEscritorios = punto.dato.getEscritorios()
                                #cantidad = listaEscritorios.longitud()
                                listaEscritorios = punto.dato.getEscritorios().valores()
                                escritoriosActivos = 0
                                escritoriosInactivos = 0
                                while listaEscritorios != None:
                                    if listaEscritorios.dato.getEstado() == True:
                                        escritoriosActivos += 1
                                    else:
                                        escritoriosInactivos += 1
                                    #print("|", listaEscritorios.dato.getId(), (9-len(str(listaEscritorios.dato.getId())))*(" "), "|")
                                    #print("|", empresaEnLista.dato.getId(), (9-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(), (19-len(empresaEnLista.dato.getNombre()))*(" "), ("|"))
                                    listaEscritorios = listaEscritorios.siguiente
                                print("Escritorios activos:",str(escritoriosActivos))
                                print("Escritorios inactivos:",str(escritoriosInactivos))
                    else:
                        print("¡Sistema vacio!")
                elif opcion == 3:
                    print(" -----------Manejo de Puntos de Atencion--------- ")
                    print("| 1. Ver Estado del Punto de Atencion            |")
                    print("| 2. Activar Escritorio de Servicio              |")
                    print("| 3. Desactivar Escritorio                       |")
                    print("| 4. Atender Cliente                             |")
                    print("| 5. Solicitud de Atencion:                      |")
                    print("| 6. Simular Actividad del Punto de Atencion     |")
                    print(" ------------------------------------------------ ")
                elif opcion == 4:
                    self.listaEmpresas = listaEnlazada()
                    print("¡Sistema limpiado exitosamente!")              
                elif opcion == 5:
                    print("¡Ejecucion Finalizada!")
                    break
                elif opcion == 6:
                    empresaEnLista = self.listaEmpresas.valores()
                    while empresaEnLista != None:
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
                            transaccionesEnLista = transaccionesEnLista.siguiente
                        empresaEnLista = empresaEnLista.siguiente
                else:
                    print("¡Ingrese una opcion valida!")
            except ValueError:
                print("¡Ingrese solo numeros!")

menuPrincipal()