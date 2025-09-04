"""Utilizando la función creada en el ejercicio 2, desarrollar un programa para crear dos matrices
de 3x3 con valores al azar entre dos números ingresados por teclado. Verificar que el rango
sea válido, caso contrario solicitar nuevamente ambos valores. Calcular la suma de sus
elementos y mostrar la matriz resultante."""
import random

def imprimirmatriz(mat):
    tamaño = len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            print(mat[ff][cc], end=" ")
        print()
    print()

def rellenarmatriz(rango,mat):
    a=int(input("Ingrese un valor minimo:"))
    b=int(input("Ingrese un valor maximo:"))
    for ff in range(rango):
        for cc in range(rango):
            mat[ff][cc] = random.randint(a,b)

def sumaelementos(mat):
    total=0
    tamaño=len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            total= total + mat[ff][cc]
    return total

#Programa principal

matriz1= []
a=3
for f in range(a):
    matriz1.append([])
    for c in range(a):
        matriz1[f].append(0)
matriz2=[]
for f in range(a):
    matriz2.append([])
    for c in range(a):
        matriz2[f].append(0)

rellenarmatriz(a,matriz1)
imprimirmatriz(matriz1)
rellenarmatriz(a,matriz2)
imprimirmatriz(matriz2)
print("La suma de los elementos de la matriz 1 es: ",sumaelementos(matriz1))
print("La suma de los elementos de la matriz 2 es: ",sumaelementos(matriz2))

