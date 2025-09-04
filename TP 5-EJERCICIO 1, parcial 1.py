"""
Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999.
Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100).

"""

menordeEdad=0
mayordeEdad=0
promediototal=0
contar=1

edad=int(input("Ingresar la edad de la persona o ingresar 999 para terminar:"))

while edad == 999 and( edad > 0 or edad <100):
    print("Error ! ---- El valor debe ser valido")
    edad=int(input("Ingresar la edad de la persona o ingresar 999 para terminar:"))
   
while edad !=999:
    if edad >=18:
        mayordeEdad= mayordeEdad + 1
        promediototal= promediototal + 1
        contar= contar + edad
        edad=int(input("Ingresar la edad de la persona o ingresar 999 para terminar:"))
        
    else:
        menordeEdad= menordeEdad + 1
        promediototal= promediototal + 1
        contar= contar + edad 
        edad=int(input("Ingresar la edad de la persona o ingresar 999 para terminar:"))

print("El promedio de edad de ambos grupos es: " , contar/promediototal)
        