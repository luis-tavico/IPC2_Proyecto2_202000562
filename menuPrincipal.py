from decimal import DivisionUndefined
from cargarArchivo import CargarArchivo
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloCliente import Cliente
from modeloEscritorio import Escritorio
from modeloTransaccion import Transaccion
from graphviz import Grafico

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
            print("| 3. Limpiar Sistema                             |")
            print("| 4. Salir                                       |")
            print(" ------------------------------------------------ ")
            try:
                opcion = int(input("Ingrese una opcion: "))
                if opcion == 1:
                    menu = True
                    while menu:
                        print(" -----------Configuracion de Empresas------------ ")
                        print("| 1. Cargar Archivo de Configuracion del Sistema |")
                        print("| 2. Cargar Archivo con Configuracion Inicial    |")
                        print("| 3. Crear/Editar Empresa                        |")
                        print("| 4. Regresar al Menu Principal                  |")
                        print(" ------------------------------------------------ ")
                        try:
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                #ConfiguracionSistema.xml
                                #ruta = input("Ingrese la ruta del archivo -> ")
                                ruta = "ConfiguracionSistema2.xml"
                                archivo = CargarArchivo()
                                archivo.leerArchivoConfiguracionSistema(ruta, self.listaEmpresas)
                            elif opcion == 2:
                                if self.listaEmpresas.valores() != None:
                                #ConfiguracionInicial.xml
                                #ruta = input("Ingrese la ruta del archivo -> ")
                                    ruta = "ConfiguracionInicial2.xml"
                                    archivo = CargarArchivo()
                                    archivo.leerArchivoConfiguracionInicial(ruta, self.listaEmpresas)  
                                else: print("¡Sistema vacio!")                                
                            elif opcion == 3:   
                                print(" ------------------Crear/Editar------------------ ")                          
                                print("| 1. Crear Empresa                               |")
                                print("| 2. Editar Empresa                              |")
                                print("| 3. Regresar a Configuracion de Empresas        |")
                                print(" ------------------------------------------------ ")
                                opcion = int(input("Ingrese una opcion: "))
                                if opcion < 1 or opcion > 3:
                                    print("¡Ingrese una opcion valida!")
                                    continue
                                elif opcion == 3: continue
                                elif opcion == 1:
                                    print("------------Nueva Empresa-------------")
                                    idEmpresa = input("Ingrese el id de la empresa: ")
                                    nombreEmpresa = input("Ingrese el nombre de la empresa: ")
                                    abreviatura = input("Ingrese la abreviatura de la empresa: ")
                                    empresa = Empresa(idEmpresa, nombreEmpresa, abreviatura, listaEnlazada(), listaEnlazada())
                                    self.listaEmpresas.insertar(empresa)
                                    empresa = self.listaEmpresas.buscarId(idEmpresa)
                                elif opcion == 2:
                                    resultado = self.mostrarEmpresas()
                                    if resultado:
                                        posicion = int(input("Ingrese un numero: "))                                 
                                        empresa = self.listaEmpresas.buscarPosicion(posicion)
                                    else: continue
                                if empresa != None:
                                    listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()
                                    listaTransacciones = empresa.dato.getTransacciones()
                                else: continue
                                while True:
                                    print(" --------------------Agregar--------------------- ")
                                    print("| 1. Transacciones                               |")
                                    print("| 2. Punto de Atencion                           |")
                                    print("| 3. Escritorios de Servicio                     |")
                                    print("| 4. Regresar a Configuracion de Empresas        |")
                                    print("| 5. Regresar al Menu Principal                  |")
                                    print(" ------------------------------------------------ ")
                                    try: 
                                        opcion = int(input("Ingrese una opcion: "))
                                        if opcion == 1:   
                                            print("----------Nueva Transaccion-----------")
                                            idTransaccion = input("Ingrese el id de la transaccion: ")
                                            nombreTransaccion = input("Ingrese el nombre de la transaccion: ")    
                                            tiempoTransaccion = input("Ingrese el tiempo de la transaccion: ")         
                                            transaccion = Transaccion(id=idTransaccion, nombre=nombreTransaccion, tiempo=tiempoTransaccion)
                                            listaTransacciones.insertar(transaccion)
                                            print("¡Transaccion agregada exitosamente!")                          
                                        elif opcion == 2:  
                                            print("-------Nuevo Punto de Atencion--------")
                                            idPuntoAtencion = input("Ingrese el id del punto de atencion: ")
                                            nombrePuntoAtencion = input("Ingrese el nombre del punto de atencion: ")
                                            direccionPuntoAtencion = input("Ingrese la direccion del punto de atencion: ")   
                                            puntoAtencion = PuntoAtencion(idPuntoAtencion, nombrePuntoAtencion, direccionPuntoAtencion, listaEnlazada(), listaEnlazada(), listaEnlazada())
                                            listaPuntosAtencion.insertar(puntoAtencion) 
                                            print("¡Punto de atencion agregado exitosamente!")                    
                                        elif opcion == 3: 
                                            resultado = self.mostrarPuntosAtencion(listaPuntosAtencion)
                                            if resultado:
                                                posicion = int(input("Ingrese un numero: "))
                                                listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()                         
                                                punto = listaPuntosAtencion.buscarPosicion(posicion)
                                            else: continue 
                                            if punto != None:
                                                listaEscritorios = punto.dato.getEscritorios()                             
                                                print("-----Nuevo Escritorio de Servicio-----")
                                                idEscritorio = input("Ingrese el id del escritorio: ")
                                                identificacionEscritorio = input("Ingrese la identificacion del escritorio: ")
                                                nombreEncargado = input("Ingrese el nombre del encargado del escritorio: ")
                                                escritorio = Escritorio(idEscritorio, identificacionEscritorio, nombreEncargado, False, listaEnlazada())
                                                listaEscritorios.insertar(escritorio)                                          
                                                print("¡Escritorio de servicio agregados exitosamente!")
                                        elif opcion == 4: break
                                        elif opcion == 5:
                                            menu = False
                                            break
                                        else: 
                                            print("¡Ingrese una opcion valida!")
                                    except ValueError:
                                        print("¡Ingrese solo numeros!")                                   
                            elif opcion == 4: break
                            else: 
                                print("¡Ingrese una opcion valida!")
                        except ValueError:
                            print("¡Ingrese solo numeros!")
                        except FileNotFoundError:
                            print("¡El archivo no existe!")                     
                elif opcion == 2:
                    #ConfiguracionSistema2.xml
                    #ConfiguracionInicial2.xml
                    resultado = self.mostrarEmpresas()
                    if resultado == False: continue
                    posicion = int(input("Ingrese un numero: "))                                 
                    empresa = self.listaEmpresas.buscarPosicion(posicion)
                    if empresa == None: continue
                    listaTransacciones = empresa.dato.getTransacciones()
                    listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()
                    resultado = self.mostrarPuntosAtencion(listaPuntosAtencion)
                    if resultado == False: continue
                    posicion = int(input("Ingrese un numero: "))
                    listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()                         
                    punto = listaPuntosAtencion.buscarPosicion(posicion)
                    if punto == None: continue
                    while True:
                        print(" ----------Manejo de Puntos de Atencion---------- ")
                        print("| 1. Ver Estado                                  |")
                        print("| 2. Activar Escritorio de Servicio              |")
                        print("| 3. Desactivar Escritorio                       |")
                        print("| 4. Atender Cliente                             |")
                        print("| 5. Solicitud de Atencion                       |")
                        print("| 6. Simular Actividad                           |")
                        print("| 7. Regresar al Menu Principal                  |")
                        print(" ------------------------------------------------ ")
                        try:
                            opcion = int(input("Ingrese una opcion: "))
                            if opcion == 1:
                                listaEscritorios = punto.dato.getEscritorios()
                                if punto.dato.getClientes() != None:
                                    listaClientes = punto.dato.getClientes().valores()
                                    tiempo = 0                  
                                    tiempoMinEspera = 0
                                    tiempoPromEspera = 0
                                    tiempoMaxEspera = 0
                                    while listaClientes != None:
                                        listaTransaccionesCliente = listaClientes.dato.getTransacciones().valores()
                                        tiempo = 0
                                        while listaTransaccionesCliente != None: 
                                            transaccion = listaTransacciones.buscarId(listaTransaccionesCliente.dato.getId())
                                            tiempo += (int(transaccion.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad())) 
                                            listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                                        if tiempoMinEspera == 0:
                                            tiempoMinEspera = tiempo
                                        tiempoPromEspera += tiempo
                                        tiempoMaxEspera += tiempo           
                                        listaClientes = listaClientes.siguiente
                                    listaClientes = punto.dato.getClientes()
                                    tiempoMaxEspera = tiempoMaxEspera - tiempo 
                                    if listaClientes.longitud() > 0:
                                        tiempoPromEspera = ((int(tiempoPromEspera))/listaClientes.longitud())
                                    tiempoMinEspera = self.convertirTiempo(tiempoMinEspera)
                                    tiempoMaxEspera = self.convertirTiempo(tiempoMaxEspera)
                                    tiempoPromEspera = self.convertirTiempo(tiempoPromEspera)
                                    print("Tiempo:", tiempo, "minutos")
                                    print("Tiempo Espera Minimo:", tiempoMinEspera)
                                    print("Tiempo Espera Promedio:", tiempoPromEspera)
                                    print("Tiempo Espera Maximo:", tiempoMaxEspera)
                                    print("Clientes en espera de atencion:", listaClientes.longitud())
                                listaEscritorios = punto.dato.getEscritorios().valores()
                                escritoriosActivos = 0
                                escritoriosInactivos = 0
                                tiempoMinAtencion = 0
                                tiempoPromAtencion = 0
                                tiempoMaxAtencion = 0
                                while listaEscritorios != None:
                                    listaclientesAtendidos = listaEscritorios.dato.getClientesAtendidos().valores()
                                    while listaclientesAtendidos != None:
                                        listaTransaccionesCliente = listaclientesAtendidos.dato.getTransacciones().valores()
                                        tiempo = 0
                                        while listaTransaccionesCliente != None:
                                            transaccion = listaTransacciones.buscarId(listaTransaccionesCliente.dato.getId())
                                            tiempo += (int(transaccion.dato.getTiempo())*int(listaTransacciones.dato.getCantidad()))
                                            listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                                        tiempoPromAtencion += tiempo
                                        if tiempo > tiempoMaxAtencion:
                                            tiempoMaxAtencion = tiempo
                                        if tiempoMinAtencion == 0:
                                            tiempoMinAtencion = tiempo
                                        if tiempo < tiempoMinAtencion:
                                            tiempoMinAtencion = tiempo
                                        listaclientesAtendidos = listaclientesAtendidos.siguiente
                                    if listaEscritorios.dato.getEstado() == True:
                                        escritoriosActivos += 1
                                    else:
                                        escritoriosInactivos += 1
                                    listaEscritorios = listaEscritorios.siguiente
                                print("Escritorios activos:",str(escritoriosActivos))
                                print("Escritorios inactivos:",str(escritoriosInactivos))
                                if listaClientes.longitud() > 0:
                                    tiempoPromAtencion = ((int(tiempoPromAtencion))/listaClientes.longitud())                                 
                                tiempoPromAtencion = self.convertirTiempo(tiempoPromAtencion)
                                tiempoMinAtencion = self.convertirTiempo(tiempoMinAtencion)
                                tiempoMaxAtencion = self.convertirTiempo(tiempoMaxAtencion)
                                print("Tiempo:", tiempo, "minutos")
                                print("Tiempo Atencion Minimo:", tiempoMinAtencion)
                                print("Tiempo Atencion Promedio:", tiempoPromAtencion)
                                print("Tiempo Atencion Maximo:", tiempoMaxAtencion)
                                graficar = Grafico()
                                graficar.encabezado(empresa.dato.getNombre().upper())
                                graficar.puntoAtencion(punto.dato.getNombre(), escritoriosActivos, escritoriosInactivos, listaClientes.longitud(), tiempoMinEspera, tiempoPromEspera, tiempoMaxEspera, tiempoMinAtencion, tiempoPromAtencion, tiempoMaxAtencion)
                                listaEscritoriosActivos = punto.dato.getEscritoriosActivos().valores()
                                numero = 0
                                while listaEscritoriosActivos != None:
                                    numero += 1
                                    clientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos().longitud()
                                    listaclientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos().valores()
                                    tiempoMinAtencion = 0
                                    tiempoPromAtencion = 0
                                    tiempoMaxAtencion = 0
                                    while listaclientesAtendidos != None:
                                        listaTransaccionesCliente = listaclientesAtendidos.dato.getTransacciones().valores()
                                        tiempo = 0
                                        while listaTransaccionesCliente != None:
                                            transaccion = listaTransacciones.buscarId(listaTransaccionesCliente.dato.getId())
                                            tiempo += (int(transaccion.dato.getTiempo())*int(listaTransacciones.dato.getCantidad()))
                                            listaTransaccionesCliente = listaTransaccionesCliente.siguiente  
                                        tiempoPromAtencion += tiempo
                                        if clientesAtendidos > 0:
                                            tiempoPromAtencion = int(tiempoPromAtencion/clientesAtendidos)
                                        if tiempo > tiempoMaxAtencion:
                                            tiempoMaxAtencion = tiempo
                                        if tiempoMinAtencion == 0:
                                            tiempoMinAtencion = tiempo
                                        if tiempo < tiempoMinAtencion:
                                            tiempoMinAtencion = tiempo
                                        listaclientesAtendidos = listaclientesAtendidos.siguiente
                                    tiempoPromAtencion = self.convertirTiempo(tiempoPromAtencion)
                                    tiempoMinAtencion = self.convertirTiempo(tiempoMinAtencion)
                                    tiempoMaxAtencion = self.convertirTiempo(tiempoMaxAtencion)
                                    graficar.escritorio(numero, listaEscritoriosActivos.dato.getIdentificacionEscritorio(), tiempoMinAtencion, tiempoPromAtencion, tiempoMaxAtencion, clientesAtendidos)
                                    listaEscritoriosActivos = listaEscritoriosActivos.siguiente                                
                                    '''print("Tiempo:", tiempo, "minutos")
                                    print("Tiempo Atencion Minimo:", tiempoMinAtencion)
                                    print("Tiempo Atencion Promedio:", tiempoPromAtencion)
                                    print("Tiempo Atencion Maximo:", tiempoMaxAtencion)'''
                                graficar.exportar()
                            elif opcion == 2:
                                listaEscritorios = punto.dato.getEscritorios().valores()
                                listaEscritoriosActivos = punto.dato.getEscritoriosActivos()
                                while listaEscritorios != None:
                                    if listaEscritorios.dato.getEstado() == False:
                                        listaEscritorios.dato.setEstado(True)
                                        listaEscritoriosActivos.insertar(listaEscritorios.dato)
                                        print("¡Escritorio Activado Exitosamente!")
                                        break
                                    listaEscritorios = listaEscritorios.siguiente
                            elif opcion == 3:
                                listaEscritorios = punto.dato.getEscritorios()
                                listaEscritoriosActivos = punto.dato.getEscritoriosActivos()
                                escritorio = listaEscritoriosActivos.eliminarUltimo()
                                if escritorio != None:
                                    escritorio = listaEscritorios.buscarId(escritorio.dato.getId())
                                    escritorio.dato.setEstado(False)
                                    print("¡Escritorio Desactivado Exitosamente!")
                                else:
                                    print("¡No hay escritorios activos!")
                            elif opcion == 4:
                                listaEscritoriosActivos = punto.dato.getEscritoriosActivos().valores()
                                listaClientes = punto.dato.getClientes()
                                while listaEscritoriosActivos != None:
                                    listaclientesAtendidos = listaEscritoriosActivos.dato.getClientesAtendidos()
                                    if listaClientes.longitud() > 0:
                                        clienteAtendido = listaClientes.eliminarPrimero()
                                        listaclientesAtendidos.insertar(clienteAtendido.dato)
                                        print(str(listaClientes.longitud()))                                                                      
                                    else: break  
                                    listaEscritoriosActivos = listaEscritoriosActivos.siguiente
                            elif opcion == 5:
                                listaTransaccionesCliente = listaEnlazada()
                                while True:
                                    resultado = self.mostrarTransacciones(listaTransacciones)
                                    if resultado == False: break
                                    posicion = int(input("Ingrese un numero: "))                                               
                                    listaTransacciones = empresa.dato.getTransacciones()
                                    transaccion = listaTransacciones.buscarPosicion(posicion)
                                    if transaccion == None: continue
                                    cantidad = int(input("Ingrese la cantidad de veces que realizara la transaccion: "))
                                    nuevaTransaccion = Transaccion(id=transaccion.dato.getId(), nombre=transaccion.dato.getNombre(), tiempo=transaccion.dato.getTiempo(), cantidad=cantidad)
                                    listaTransaccionesCliente.insertar(nuevaTransaccion)
                                    confirmacion = input("¿Desea agregar otra transaccion? (s/n) ")
                                    if confirmacion == 'n': break                
                                #print(transaccion.dato.getTiempo())
                                dpiCliente = input("Ingrese su DPI: ")
                                nombreCliente = input("Ingrese su nombre: ")
                                cliente = Cliente(dpiCliente, nombreCliente, listaTransaccionesCliente)
                                listaClientes = punto.dato.getClientes()
                                listaClientes.insertar(cliente)
                                ##################################################
                                #print(listaTransacciones.dato.getId())  
                                punto.dato.setTurnoEnPunto()
                                print("Su turno es -> |",str(punto.dato.getTurnoEnPunto()),"|")
                                listaClientes = punto.dato.getClientes().valores()
                                tiempo = 0
                                tiempoEnCola = 0
                                tiempoEnEscritorio = 0
                                tiempoTotal = 0
                                listaTransaccionesCliente = listaTransaccionesCliente.valores()
                                while listaTransaccionesCliente != None:
                                    transaccion = listaTransacciones.buscarId(listaTransaccionesCliente.dato.getId())
                                    tiempoEnEscritorio += (int(transaccion.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad()))
                                    listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                                while listaClientes != None:
                                    listaTransaccionesCliente = listaClientes.dato.getTransacciones().valores()
                                    tiempo = 0
                                    while listaTransaccionesCliente != None:  
                                        transaccion = listaTransacciones.buscarId(listaTransaccionesCliente.dato.getId())
                                        tiempo += (int(transaccion.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad()))
                                        listaTransaccionesCliente = listaTransaccionesCliente.siguiente                                  
                                    listaClientes = listaClientes.siguiente
                                    tiempoEnCola += tiempo
                                tiempoTotal = tiempoEnCola
                                tiempoEnCola = tiempoEnCola - tiempoEnEscritorio
                                tiempoEnCola = self.convertirTiempo(tiempoEnCola)
                                tiempoEnEscritorio = self.convertirTiempo(tiempoEnEscritorio)
                                tiempoTotal = self.convertirTiempo(tiempoTotal)
                                print("Tiempo en cola:", tiempoEnCola)
                                print("Tiempo en escritorio:", tiempoEnEscritorio)
                                print("Tiempo total:", tiempoTotal)
                            elif opcion == 7: break
                            else: 
                                print("¡Ingrese una opcion valida!")
                        except FileExistsError:
                            print("error")
                elif opcion == 3:
                    self.listaEmpresas = listaEnlazada()
                    print("¡Sistema limpiado exitosamente!")              
                elif opcion == 4:
                    print("¡Ejecucion Finalizada!")
                    break
                elif opcion == 5:
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
                    #except Exception as e:
                    print("¡Ingrese una opcion valida!")
            except ValueError:
                print("¡Ingrese solo numeros!")

    def mostrarEmpresas(self):         
        if self.listaEmpresas.valores() != None:
            numero = 0
            empresaEnLista = self.listaEmpresas.valores()
            print(" ------------------------------------------------------------------- ")
            print("| No. |     Id        |        Nombre        |     Abreviatura      |")
            print("|-------------------------------------------------------------------|")
            while empresaEnLista != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", empresaEnLista.dato.getId(), (12-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(),
                (19-len(empresaEnLista.dato.getNombre()))*(" "), ("|"), empresaEnLista.dato.getAbreviatura(), (19-len(str(empresaEnLista.dato.getAbreviatura())))*(" "), "|")
                empresaEnLista = empresaEnLista.siguiente
            print(" ------------------------------------------------------------------- ")
            return True
        else:
            print("¡Sistema vacio!")
            return False
    
    def mostrarPuntosAtencion(self, listaPuntosAtencion):
        if listaPuntosAtencion.valores() != None:
            numero = 0
            listaPuntosAtencion = listaPuntosAtencion.valores()   
            print(" ------------------------------------------------------------------ ")
            print("| No. |     Id        |        Nombre        |      Direccion      |")
            print("|------------------------------------------------------------------|")
            while listaPuntosAtencion != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", listaPuntosAtencion.dato.getId(), (12-len(str(listaPuntosAtencion.dato.getId())))*(" "), "|", listaPuntosAtencion.dato.getNombre(), 
                (19-len(listaPuntosAtencion.dato.getNombre()))*(" "), "|", listaPuntosAtencion.dato.getDireccion(), (18-len(listaPuntosAtencion.dato.getDireccion()))*(" "), ("|"))
                listaPuntosAtencion = listaPuntosAtencion.siguiente
            print(" ------------------------------------------------------------------ ")
            return True
        else:
            print("¡Sin puntos de atencion!")
            return False

    def mostrarTransacciones(self, listaTransacciones):
        if listaTransacciones.valores() != None:
            numero = 0
            listaTransacciones = listaTransacciones.valores()
            print(" ----------------------------------------------------- ")
            print("| No. |     Id        |        Nombre        | Tiempo |")
            print("|-----------------------------------------------------|")
            while listaTransacciones != None:
                numero += 1
                print("|", numero, (2-len(str(numero)))*(" "), "|", listaTransacciones.dato.getId(), (12-len(str(listaTransacciones.dato.getId())))*(" "), "|", listaTransacciones.dato.getNombre(), 
                (19-len(listaTransacciones.dato.getNombre()))*(" "), "|", listaTransacciones.dato.getTiempo(), (5-len(listaTransacciones.dato.getTiempo()))*(" "), ("|"))
                listaTransacciones = listaTransacciones.siguiente
            print(" ----------------------------------------------------- ")
            return True
        else:
            print("¡Sin transacciones!")
            return False

    def convertirTiempo(self, tiempo):
        tiempo = int(tiempo)
        hora = int((tiempo-(tiempo%60))/60)
        minuto = tiempo%60
        tiempo = ""
        if hora == 1:
            tiempo += str(hora)+" hora "
        elif hora > 1:
            tiempo += str(hora)+" horas "
        if minuto == 1:
            tiempo += str(minuto)+" minuto"
        elif minuto > 1:
            tiempo += str(minuto)+" minutos"
        if tiempo == "":
            return "0"
        else:
            return tiempo

menuPrincipal()