#FUNCION 1
def leerentero(minimo,maximo):
    print("Ingresar un valor entre", minimo, "y", maximo)
    a=int(input())
    while a < minimo or a> maximo:
        print("Valor incorrecto")
        print("El valor debe estar entre",minimo,"y",maximo)
        a= int(input("Ingresar un numero entero:"))
    return a

#FUNCION 2

def calcularedad(dnac,mnac,anac,dact,mact,aact):
    edad= aact - anac
    if mact < mnac:
        edad= edad - 1
    elif mact == mnac and dact < dnac:
        edad=edad - 1
    return edad

#FUNCION 3
def leerfecha():
    print("Dia?")
    dia=leerentero(1,31)
    print("Mes?")
    mes=leerentero(1,12)
    print("Año?")
    año=leerentero(1500,2100)
    return dia, mes, año

#PROGRAMA PRINCIPAL
print("Ingresa tu fecha de nacimiento:")
dnac,mnac,anac= leerfecha()
print("Ingresa la fecha de hoy:")
dhoy,mhoy,ahoy= leerfecha()
edad= calcularedad(dnac, mnac, anac, dhoy, mhoy, ahoy)
print("Tenes", edad, "años")