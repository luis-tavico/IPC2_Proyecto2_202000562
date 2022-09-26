def convertirTiempo(tiempo):
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
        

print(convertirTiempo(183))