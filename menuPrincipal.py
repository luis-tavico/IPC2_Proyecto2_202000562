from cargarArchivo import CargarArchivo

class menuPrincipal():

    while True:
        print(" -----------------Menu Principal----------------- ")
        print("| 1. Configuracion de Empresas                   |")
        print("| 2. Selección de Empresa y Punto de Atencion    |")
        print("| 3. Manejo de Puntos de Atencion                |")
        print("| 4. Salir                                       |")
        print(" ------------------------------------------------ ")
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                while True:
                    print(" -----------Configuracion de Empresas------------ ")
                    print("| 1. Limpiar Sistema                             |")
                    print("| 2. Cargar Archivo de Configuracion del Sistema |")
                    print("| 3. Crear Nueva Empresa                         |")
                    print("| 4. Cargar Archivo con Configuración Inicial    |")
                    print("| 5. Regresar al Menu Principal                  |")
                    print(" ------------------------------------------------ ")
                    try:
                        opcion = int(input("Ingrese una opcion: "))
                        if opcion == 1:
                            print()
                        elif opcion == 2:
                            #configuracionInicial.xml
                            ruta = input("Ingrese la ruta del archivo -> ")
                            archivo = CargarArchivo()
                            archivo.leerArchivoConfiguracionSistema(ruta)
                        elif opcion == 3:
                            while True:
                                print(" --------------Crear Nueva Empresa--------------- ")
                                print("| 1. Puntos de Atencion                          |")
                                print("| 2. Escritorios de Servicio                     |")
                                print("| 3. Transacciones                               |")
                                print("| 4. Regresar a Configuracion de Empresas        |")
                                print(" ------------------------------------------------ ")
                                try:
                                    opcion = int(input("Ingrese una opcion: "))
                                    if opcion == 1:
                                        print()
                                    elif opcion == 2:
                                        print()
                                    elif opcion == 3:
                                        print()
                                    elif opcion == 4:
                                        break
                                    else: 
                                        print("¡Ingrese una opcion valida!")
                                except ValueError:
                                    print("¡Ingrese solo numeros!")
                        elif opcion == 4:
                            #configuracionSistema.xml
                            ruta = input("Ingrese la ruta del archivo -> ")
                            archivo = CargarArchivo()
                            archivo.leerArchivoConfiguracionInicial(ruta)
                        elif opcion == 5:
                            break
                        else: 
                            print("¡Ingrese una opcion valida!")
                    except ValueError:
                        print("¡Ingrese solo numeros!")
            elif opcion == 2:
                print("")
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
                print("¡Ejecucion Finalizada!")
                break
            else:
                print("¡Ingrese una opcion valida!")
        except ValueError:
            print("¡Ingrese solo numeros!")

menuPrincipal()