#Leer 10 números enteros e imprimir el promedio, el mayor y en qué orden fue ingresado el mayor valor.si se ingresó más de una vez debe informar el primer ingreso.

num=int(input("Ingresar un numero entero:"))
cont=1
suma= 0
mayor=num
posicion=1


while cont < 10:
    suma= suma+num
    cont= cont+1
    num= int(input("Ingresar un numero entero:"))
    
    if num > mayor:
        mayor=num
        posicion=cont
    
print("El promedio es: ", suma/10)
print("El mayor numero ingresado es:",mayor, "en la posicion:" , posicion)
    
