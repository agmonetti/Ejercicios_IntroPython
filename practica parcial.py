def porcentaje(cant,contar):
    porcentaje_total = (cant * 100) // (contar)
    return porcentaje_total

def cual_aparece(cant1,cant2,cant3,cant4):
    if (cant1 > cant4 and cant1 > cant3 and cant1 > cant2):
        print("El que mas aparece es el niño")
    if (cant2 > cant4 and cant2 > cant3 and cant2 > cant3):
        print("El que mas aparece es el adolescente")
    if(cant3 > cant4 and cant3 > cant1 and cant3 > cant2):
        print("El que mas aparece es el adulto")
    if(cant4 > cant1 and cant4 > cant3 and cant4 > cant2):
        print("El que mas aparece es el anciano")

edad = 1
contar = 0
cant_niño = 0
cant_adolescente = 0
cant_adulto = 0
cant_anciano = 0
mas_poblado= "ninguno"

while(edad != -1):

    edad=int(input("Cual es su edad"))
    contar = contar+1

    if (edad < -1):
        print("El numero es invalido")
        contar = contar-1

    if(edad <= 12 and edad > 0):
        print("Es un pequeño niño")
        cant_niño = cant_niño+1

    elif(edad >= 13 and edad <= 20):
        print("Es un adolescente")
        cant_adolescente = cant_adolescente + 1

    elif(edad >= 21 and edad <= 69):
        print("Es un adulto")
        cant_adulto = cant_adulto + 1

    elif(edad >= 70):
        print("Es un anciano")
        cant_anciano = cant_anciano+1

contar=contar-1

print("El porcentaje de niños", porcentaje(cant_niño,contar), "%")

print("El porcentaje de adolescentes",porcentaje(cant_adolescente,contar), "%")

print("El porcentaje de adultos",porcentaje(cant_adulto,contar) , "%")

print("El porcentaje de ancianos", porcentaje(cant_anciano,contar),"%")

cual_aparece(cant_niño,cant_adolescente,cant_adulto,cant_anciano)