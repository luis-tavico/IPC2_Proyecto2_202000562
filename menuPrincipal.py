from cargarArchivo import CargarArchivo
from listaEnlazada import listaEnlazada
from modeloEmpresa import Empresa
from modeloPuntoAtencion import PuntoAtencion
from modeloCliente import Cliente
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
                        print("| 3. Crear Nueva Empresa                         |")
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
                                #ConfiguracionInicial.xml
                                #ruta = input("Ingrese la ruta del archivo -> ")
                                ruta = "ConfiguracionInicial2.xml"
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
                                                #iden = input("Ingrese el nombre: ")
                                                nombre = input("Ingrese el nombre: ")    
                                                tiempo = input("Ingrese el tiempo: ")         
                                                respuesta = input("¿Desea agregar otra transaccion? (s/n) ")
                                                transaccion = Transaccion(id=idTransaccion, nombre=nombre, tiempo=tiempo)
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
                    numero = 0
                    if self.listaEmpresas.valores() != None:
                        empresaEnLista = self.listaEmpresas.valores()
                        print(" -------------------------------------------- ")
                        print("| No. |     Id        |        Nombre        |")
                        print("|--------------------------------------------|")
                        while empresaEnLista != None:
                            numero += 1
                            print("|", numero, (2-len(str(numero)))*(" "), "|", empresaEnLista.dato.getId(), (12-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(),
                            (19-len(empresaEnLista.dato.getNombre()))*(" "), ("|"))
                            empresaEnLista = empresaEnLista.siguiente
                        print(" -------------------------------------------- ")
                        posicion = int(input("Ingrese un numero: "))                                 
                        empresa = self.listaEmpresas.buscarPosicion(posicion)
                        numero = 0
                        if empresa != None:            
                            listaTransaccionesEnEmpresa = empresa.dato.getTransacciones()
                            listaPuntosAtencion = empresa.dato.getPuntosDeAtencion().valores()
                            print(" ------------------------------------------------------------------ ")
                            print("| No. |     Id        |        Nombre        |      Direccion      |")
                            print("|------------------------------------------------------------------|")
                            while listaPuntosAtencion != None:
                                numero += 1
                                print("|", numero, (2-len(str(numero)))*(" "), "|", listaPuntosAtencion.dato.getId(), (12-len(str(listaPuntosAtencion.dato.getId())))*(" "), "|", listaPuntosAtencion.dato.getNombre(), 
                                (19-len(listaPuntosAtencion.dato.getNombre()))*(" "), "|", listaPuntosAtencion.dato.getDireccion(), (18-len(listaPuntosAtencion.dato.getDireccion()))*(" "), ("|"))
                                listaPuntosAtencion = listaPuntosAtencion.siguiente
                            print(" ------------------------------------------------------------------ ")
                            posicion = int(input("Ingrese un numero: "))
                            listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()                         
                            punto = listaPuntosAtencion.buscarPosicion(posicion)
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
                                        if punto != None:
                                            listaEscritorios = punto.dato.getEscritorios()
                                            if punto.dato.getClientes() != None:
                                                listaClientes = punto.dato.getClientes().valores()
                                                tiempo = 0                  
                                                tiempoMinAtencion = 0
                                                tiempoPromAtencion = 0
                                                tiempoMaxAtencion = 0
                                                tiempoMinEspera = 0
                                                tiempoPromEspera = 0
                                                tiempoMaxEspera = 0
                                                while listaClientes != None:
                                                    listaTransacciones = listaClientes.dato.getTransacciones().valores()
                                                    tiempo = 0
                                                    while listaTransacciones != None:
                                                        #print(listaTransacciones.dato.getId())   
                                                        tra = listaTransaccionesEnEmpresa.buscarId(listaTransacciones.dato.getId())
                                                        #print(tra.dato.getTiempo())
                                                        tiempo += (int(tra.dato.getTiempo())*int(listaTransacciones.dato.getCantidad())) 
                                                        listaTransacciones = listaTransacciones.siguiente
                                                    if tiempoMinEspera == 0:
                                                        tiempoMinEspera = tiempo
                                                    tiempoPromAtencion += tiempo
                                                    tiempoMaxEspera += tiempo
                                                    if tiempo > tiempoMaxAtencion:
                                                        tiempoMaxAtencion = tiempo
                                                    if tiempoMinAtencion == 0:
                                                        tiempoMinAtencion = tiempo
                                                    if tiempo < tiempoMinAtencion:
                                                        tiempoMinAtencion = tiempo
                                                    listaClientes = listaClientes.siguiente
                                                listaClientes = punto.dato.getClientes()
                                                tiempoMaxEspera = tiempoMaxEspera - tiempo 
                                                tiempoPromAtencion = ((int(tiempoPromAtencion))/listaClientes.longitud())
                                                tiempoMinEspera = self.convertirTiempo(tiempoMinEspera)
                                                tiempoMaxEspera = self.convertirTiempo(tiempoMaxEspera)
                                                tiempoPromAtencion = self.convertirTiempo(tiempoPromAtencion)
                                                tiempoMinAtencion = self.convertirTiempo(tiempoMinAtencion)
                                                tiempoMaxAtencion = self.convertirTiempo(tiempoMaxAtencion)
                                                print("Tiempo:", tiempo, "minutos")
                                                print("Tiempo Espera Minimo:", tiempoMinEspera)
                                                print("Tiempo Espera Promedio:", tiempoPromAtencion)
                                                print("Tiempo Espera Maximo:", tiempoMaxEspera)
                                                print("Tiempo Atencion Minimo:", tiempoMinAtencion)
                                                print("Tiempo Atencion Promedio:", tiempoPromAtencion)
                                                print("Tiempo Atencion Maximo:", tiempoMaxAtencion)
                                                print("Clientes en espera de atencion:", listaClientes.longitud())
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
                                    elif opcion == 2:
                                        if punto != None:
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
                                        if punto != None:
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
                                            if listaClientes.longitud() > 0:
                                                clienteAtendido = listaClientes.eliminarPrimero()
                                                print(str(listaClientes.longitud()))                                                                      
                                            else:
                                                break  
                                            listaEscritoriosActivos = listaEscritoriosActivos.siguiente
                                    elif opcion == 5:
                                        numero = 0
                                        if self.listaEmpresas.valores() != None:
                                            empresaEnLista = self.listaEmpresas.valores()
                                            print(" -------------------------------------------- ")
                                            print("| No. |     Id        |        Nombre        |")
                                            print("|--------------------------------------------|")
                                            while empresaEnLista != None:
                                                numero += 1
                                                print("|", numero, (2-len(str(numero)))*(" "), "|", empresaEnLista.dato.getId(), (12-len(str(empresaEnLista.dato.getId())))*(" "), "|", empresaEnLista.dato.getNombre(),
                                                (19-len(empresaEnLista.dato.getNombre()))*(" "), ("|"))
                                                empresaEnLista = empresaEnLista.siguiente
                                            print(" -------------------------------------------- ")
                                            posicion = int(input("Ingrese un numero: "))                                 
                                            empresa = self.listaEmpresas.buscarPosicion(posicion)
                                            numero = 0
                                            if empresa != None:            
                                                listaPuntosAtencion = empresa.dato.getPuntosDeAtencion().valores()
                                                print(" ------------------------------------------------------------------ ")
                                                print("| No. |     Id        |        Nombre        |      Direccion      |")
                                                print("|------------------------------------------------------------------|")
                                                while listaPuntosAtencion != None:
                                                    numero += 1
                                                    print("|", numero, (2-len(str(numero)))*(" "), "|", listaPuntosAtencion.dato.getId(), (12-len(str(listaPuntosAtencion.dato.getId())))*(" "), "|", listaPuntosAtencion.dato.getNombre(), 
                                                    (19-len(listaPuntosAtencion.dato.getNombre()))*(" "), "|", listaPuntosAtencion.dato.getDireccion(), (18-len(listaPuntosAtencion.dato.getDireccion()))*(" "), ("|"))
                                                    listaPuntosAtencion = listaPuntosAtencion.siguiente
                                                print(" ------------------------------------------------------------------ ")
                                                posicion = int(input("Ingrese un numero: "))
                                                listaPuntosAtencion = empresa.dato.getPuntosDeAtencion()                         
                                                punto = listaPuntosAtencion.buscarPosicion(posicion)
                                                numero = 0
                                                if punto != None:
                                                    listaTransaccionesCliente = listaEnlazada()
                                                    while True:
                                                        listaTransaccionesEnEmpresa = empresa.dato.getTransacciones().valores()                              
                                                        print(" ----------------------------------------------------- ")
                                                        print("| No. |     Id        |        Nombre        | Tiempo |")
                                                        print("|-----------------------------------------------------|")
                                                        while listaTransaccionesEnEmpresa != None:
                                                            numero += 1
                                                            print("|", numero, (2-len(str(numero)))*(" "), "|", listaTransaccionesEnEmpresa.dato.getId(), (12-len(str(listaTransaccionesEnEmpresa.dato.getId())))*(" "), "|", listaTransaccionesEnEmpresa.dato.getNombre(), 
                                                            (19-len(listaTransaccionesEnEmpresa.dato.getNombre()))*(" "), "|", listaTransaccionesEnEmpresa.dato.getTiempo(), (5-len(listaTransaccionesEnEmpresa.dato.getTiempo()))*(" "), ("|"))
                                                            listaTransaccionesEnEmpresa = listaTransaccionesEnEmpresa.siguiente
                                                        print(" ----------------------------------------------------- ")
                                                        posicion = int(input("Ingrese un numero: "))                                               
                                                        listaTransaccionesEnEmpresa = empresa.dato.getTransacciones()
                                                        transaccion = listaTransaccionesEnEmpresa.buscarPosicion(posicion)
                                                        cantidad = int(input("Ingrese la cantidad de veces que realizara la transaccion: "))
                                                        nuevaTransaccion = Transaccion(id=transaccion.dato.getId(), nombre=transaccion.dato.getNombre(), tiempo=transaccion.dato.getTiempo(), cantidad=cantidad)
                                                        listaTransaccionesCliente.insertar(nuevaTransaccion)
                                                        confirmacion = input("¿Desea agregar otra transaccion? (s/n) ")
                                                        if confirmacion == 'n':
                                                            break
                                                    #if transaccion != None:                  
                                                    #print(transaccion.dato.getTiempo())
                                                    dpiCliente = input("Ingrese su DPI: ")
                                                    nombreCliente = input("Ingrese su nombre: ")
                                                    nuevoCliente = Cliente(dpiCliente, nombreCliente, listaTransaccionesCliente)
                                                    if punto.dato.getClientes() != None:
                                                        listaClientes = punto.dato.getClientes()
                                                        listaClientes.insertar(nuevoCliente)
                                                    else:
                                                        listaClientes = listaEnlazada()
                                                        listaClientes.insertar(nuevoCliente)
                                                        punto.dato.setClientes(listaClientes)
                                                    ##################################################
                                                    #print(listaTransacciones.dato.getId())  
                                                    punto.dato.setTurnoEnPunto()
                                                    print("Su turno es -> |",str(punto.dato.getTurnoEnPunto()),"|")
                                                    listaClientes = punto.dato.getClientes().valores()
                                                    tiempoPromedio = 0
                                                    tiempoEsperado = 0
                                                    while listaClientes != None:
                                                        listaTransaccionesCliente = listaClientes.dato.getTransacciones().valores()
                                                        while listaTransaccionesCliente != None:  
                                                            transac = listaTransaccionesEnEmpresa.buscarId(listaTransaccionesCliente.dato.getId())
                                                            tiempoEsperado += (int(transac.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad()))
                                                            tiempoPromedio = (int(transac.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad()))
                                                            listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                                                        listaClientes = listaClientes.siguiente
                                                    listaClientes = punto.dato.getClientes()
                                                    print("Tiempo en cola:", str(tiempoEsperado-tiempoPromedio), "minutos")
                                                    print("Tiempo en escritorio:", str(tiempoPromedio), "minutos")
                                                    print("Tiempo total:", str(tiempoEsperado), "minutos")
                                                    '''while listaClientes != None:
                                                        listaTransaccionesCliente = listaClientes.dato.getTransacciones().valores()
                                                        while listaTransaccionesCliente != None:
                                                            #print(listaTransacciones.dato.getId())   
                                                            tra = listaTransaccionesEnEmpresa.buscarId(listaTransaccionesCliente.dato.getId())
                                                            print(tra.dato.getTiempo())
                                                            tiempo += (int(tra.dato.getTiempo())*int(listaTransaccionesCliente.dato.getCantidad()))
                                                            listaTransaccionesCliente = listaTransaccionesCliente.siguiente
                                                        listaClientes = listaClientes.siguiente
                                                    listaClientes = punto.dato.getClientes()
                                                    print("Tiempo:", tiempo, "minutos")
                                                    print("Clientes en espera de atencion:", listaClientes.longitud())
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
                                                    print("Escritorios inactivos:",str(escritoriosInactivos))'''
                                        else:
                                            print("¡Sistema vacio!")
                                    elif opcion == 7:
                                        break
                                    else: 
                                        print("¡Ingrese una opcion valida!")
                                except ZeroDivisionError:
                                    print("error")
                    else:
                        print("¡Sistema vacio!")
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
        return tiempo

menuPrincipal()