# Total recaudado por cada unidad, ordenado de mayor a menor según el monto
def recaudacionunidad(veh, tari):
    n = len(veh) - 1
    for k in range(n):
        for x in range(n):
            if tari[x] < tari[x + 1]:
                aux1 = tari[x]
                tari[x] = tari[x + 1]
                tari[x + 1] = aux1

                aux2 = veh[x]
                veh[x] = veh[x + 1]
                veh[x + 1] = aux2

    print(" ")
    print("Total recaudado por unidad")
    for x in range(len(tari)):
        print("Unidad ", veh[x], " Tarifa $", tari[x])


# Unidad que más viajes realizó
def unidadmasviajes(veh):
    n = len(veh) - 1
    for k in range(n):
        for x in range(n):
            if veh[x] > veh[x + 1]:
                aux1 = veh[x]
                veh[x] = veh[x + 1]
                veh[x + 1] = aux1
    auxtaxi = 0
    acumviajes = 0
    totviajes = 0

    for x in range(len(veh)):
        if x == 0:
            auxtaxi = veh[x]
        if auxtaxi == veh[x]:
            acumviajes = acumviajes + 1
        else:
            if acumviajes > totviajes:
                totviajes = acumviajes
                tottaxi = auxtaxi
                auxtaxi = veh[x]
    print(" ")
    print("La unidad ", tottaxi, " es la que mas viajes realizo ", totviajes)


# Importe promedio cobrado por cada unidad
# Unidad que más dinero recaudó
def unidadmasrecaudo(veh, tari):
    n = len(veh) - 1
    for k in range(n):
        for x in range(n):
            if veh[x] > veh[x + 1]:
                aux1 = veh[x]
                veh[x] = veh[x + 1]
                veh[x + 1] = aux1
                
                aux2 = tari[x]
                tari[x] = tari[x + 1]
                tari[x + 1] = aux2

    totunidad = 0
    totrecau = 0
    promedio = 0

    auxtaxi = 0
    acumrecu = 0
    totrecu = 0

    for x in range(len(veh)):
        totrecau = totrecau + tari[x]
        if x == 0:
            auxtaxi = veh[x]
            totunidd = totunidad + 1
        if auxtaxi == veh[x]:
            acumrecu = acumrecu + tari[x]
        else:
            totunidad = totunidad + 1
            if acumrecu > totrecu:
                totrecu = acumrecu
                tottaxi = auxtaxi
                auxtaxi = veh[x]
                acumrecu = tari[x]
    totunidad = totunidad + 1

    promedio = totrecau / totunidad
    print(" ")
    print("Importe promedio por unidad $", promedio)
    print(" ")
    print("La unidad ", tottaxi, " es la que mas dinero recaudo $", totrecu)


# Cantidad de viajes realizados por todas las unidades
def totalviajes(viajes):
    cantviajes = 0
    for ind in range(len(viajes)):
        cantviajes = cantviajes + 1
    print(" ")
    print("Cantidad total de viajes de la empresa ", cantviajes)


# Total general recaudado por la empresa
def totalrecaudacion(recau):
    cantrecau = 0
    for ind in range(len(recau)):
        cantrecau = cantrecau + recau[ind]
    print(" ")
    print("Total recaudado por la empresa $", cantrecau)


# Programa principal
n = int(input("Ingrese un numero de unidad entre 1 y 150 : "))
Listataxi = []
Listatarifa = []

while (n != -1):
    if (n >= 1 and n <= 150):
        Listataxi.append(n)
        t = float(input("Ingrese la tarifa del viaje : "))
        Listatarifa.append(t)
        n = int(input("Ingrese un numero de unidad entre 1 y 150 : "))
    else:
        print("Numero de unidad inválido debe ser entre 1 y 150")
        n = int(input("Ingrese un numero de unidad entre 1 y 150 : "))

recaudacionunidad(Listataxi, Listatarifa)
unidadmasrecaudo(Listataxi, Listatarifa)
unidadmasviajes(Listataxi)
totalrecaudacion(Listatarifa)
totalviajes(Listataxi)

