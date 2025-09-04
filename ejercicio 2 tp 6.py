#FUNCION

def potencia (minimo,maximo):
    print("Ingresa un numero entero entre ", minimo , "y", maximo)
    a= int(input())
    while a < minimo or a > maximo:
        print("El numero debe estar entre", minimo, "y", maximo)
        valor=int(input("Ingrese un numero entero"))
        return a


#PROGRAMA PRINCIPAL


potencia (2,10)

