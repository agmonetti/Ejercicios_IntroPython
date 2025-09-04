#Ingresar las notas de los dos parciales e indicar si promocionó, aprobo o debe recuperar.
#Si el valor de la nota no esta entre 0 y 10, debe informar un error.

#Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#Se debe recuperar cuando al menos una de las notas es menor a 4.

parcial1=int(input("Ingresar la nota del primer parcial:"))
parcial2=int(input("Ingresar la nota del segundo parcial:"))

if parcial1 >= 4 and parcial2 >=4:
    print("El alumno esta aprobado")
if parcial1 >= 7 and parcial2 >=7:
    print("El alumno promociono la materia")
if parcial1 < 4 or parcial2 < 4:
    print("El alumno debe recuperar")
if parcial1 >10 and parcial2 >10:
    print("ERROR")

