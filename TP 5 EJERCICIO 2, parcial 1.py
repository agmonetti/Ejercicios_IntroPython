"""
Escribir un algoritmo que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final.
El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4.
Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:
• Cantidad de alumnos que aprobaron con nota mayor o igual a 4.
• Cantidad de alumnos que desaprobaron el examen. Nota menor a 4.
• Porcentaje de alumnos que están aplazados (tienen 1 en el examen).
"""
nota=int(input("Ingresar la nota del alumno ó -1 para finalizar:"))
alumnosdesaprobados=0
alumnosaprobados=0
contar= 1
alumnosaplazados=0

while nota < 1 or nota > 10:
    print("Ingresar una nota valida")
    nota=int(input("Ingresar la nota del alumno ó -1 para finalizar:"))

while nota <= 10 and nota >= 1:
    if nota >=4:
        print("El alumno aprobó")
        alumnosaprobados= alumnosaprobados + 1
        nota=int(input("Ingresar la nota del alumno ó -1 para finalizar:"))
        contar= contar + 1
    elif nota <4 and nota >=2:
        print("El alumno desaprobó")
        alumnosdesaprobados= alumnosdesaprobados + 1
        nota=int(input("Ingresar la nota del alumno ó -1 para finalizar:"))
        contar= contar + 1
    else:
        print("El alumno esta aplazado")
        alumnosaplazados= alumnosaplazados + 1
        alumnosdesaprobados= alumnosdesaprobados + 1
        nota=int(input("Ingresar la nota del alumno ó -1 para finalizar:"))
        contar= contar + 1
        
print("La cantidad de alumnos aprobados es de: " , alumnosaprobados)
print("La cantidad de alumnos desaprobados es de: ", alumnosdesaprobados)

