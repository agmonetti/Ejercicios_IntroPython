#Leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
#Ejemplo: 4*3 = 4 + 4 + 4 (4 sumado 3 veces).

a=int(input("Ingresar un numero entero:"))
b=int(input("Ingresar un numero entero:"))
cont=b
mul=0

while cont>0:
    print(mul,cont)
    mul=mul+a
    cont=cont -1
    
    
print("El resultado es:", mul)