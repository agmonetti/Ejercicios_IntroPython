#Leer un numero correspondiente a un año e inprimr un mensaje si es bisiesto o no.
#Un año bisiesto es cuando es divisible por 4.
#Los años que sean divisibles x 4 y tambien x 100 no son bisiestos, a menos que sean x400 tambien

año=int(input("Ingresar un año:"))

if año%4 == 0 and año%100 == 0 and año%400 ==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

