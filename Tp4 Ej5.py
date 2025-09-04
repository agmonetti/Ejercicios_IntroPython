"""
Escribir un algoritmo que lea números enteros hasta que se ingrese un 0,
y muestre el máximo, el  mínimo  (sin  considerar  el  0)  y
la  media  (promedio)  de  todos  ellos.  Piense cómo  debe inicializar las variables
"""

n=int(input("Ingrese un numero entero (0 para terminar): "))
suma=0
cont=0
maximo=n
minimo=n

while n!=0:
    suma=suma+n
    cont=cont+1
    n=int(input("Ingrese un numero entero (0 para terminar): "))
    if n>maximo:
        maximo=n
    if n<minimo and n>0:
        minimo=n
print("La media de los numeros ingresads es de: ", suma/cont)
print("El minimo de los numeros ingresados es: ",minimo)
print("El maximo de los numeros ingresados es: ",maximo)
