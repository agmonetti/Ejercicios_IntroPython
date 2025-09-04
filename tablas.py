#Mostrar las tablas de multiplicar (entre 1 y 10) del número 4.

"""¿Cómo cambiaría el algoritmo para que el usuario pueda decidir
la tabla de multiplicar a mostrar?
"""

n= int(input("Ingresar un numero:"))
i= 1

while i <= 10:
    print( n, "x", i , "=" , n*i)
    i=i+1
    
#Pondría que n=int(input("Ingrese un numero:"))