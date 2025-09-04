#Leer dos números naturales A y B. Calcular AB mediante productos sucesivos y mostrar el resultado.
#Ejemplo: 4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).

a=int(input("Ingresar un numero entero positivo:"))
b=int(input("Ingresar un numero entero positivo:"))
cant=b
mult=1

while cant>0:
    mult= mult*a
    cant= cant -1
    
print("El resultado es:", mult)