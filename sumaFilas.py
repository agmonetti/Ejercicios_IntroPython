"""Desarrollar una función para crear una matriz de NxM (n filas y m columnas). La función recibe
n y m por parámetro, la completa con valores al azar entre a y b también por parámetro y
retorna la matriz creada. Si no hay valores entre a y b o alguna de las dimensiones es negativa,
retornar la matriz vacía. Desarrollar un pequeño programa principal crear una matriz al azar
utilizando la función y mostrar por pantalla la matriz y la suma de cada fila y cada columna"""
import random
def imprimirmatriz(mat):
    tamaño = len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            print(mat[ff][cc], end=" ")
        print()
    print()


def rellenarmatriz(filas,columnas,mat):
    a=int(input("Ingrese un valor minimo:"))
    b=int(input("Ingrese un valor maximo:"))
    if a > 0 and b > 0:
        for ff in range(filas):
            for cc in range(columnas):
                mat[ff][cc] = random.randint(a,b)
    else:
        return mat
def sumafilas(filas,mat):
    suma=0
    tamaño=len(mat)
    for i in range(filas,tamaño):
        suma = suma + mat[i]
    return suma

#Programa principal
n=int(input("Ingrese la cantidad de filas que desea: "))
m=int(input("Ingrese la cantidad de columnas que desea: "))
matriz=[]
for f in range(n):
    matriz.append([])
    for c in range(m):
        matriz[f].append(0)

imprimirmatriz(matriz)
rellenarmatriz(n,m,matriz)
print("")
imprimirmatriz(matriz)
print("La suma de todas las filas es de :",sumafilas(n,matriz))




