"""Indicar las coordenadas del
mayor valor encontrado en una matriz n*m, generada con valores aleatorios entre 100 y 1000."""

import random

def imprimirmatriz(mat):
    tamaño = len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            print(mat[ff][cc], end=" ")
        print()
    print()


def rellenarmatriz(fi,co,mat):
    a=int(input("Ingrese un valor minimo:"))
    b=int(input("Ingrese un valor maximo:"))
    for ff in range(filas):
        for cc in range(columnas):
            mat[ff][cc] = random.randint(a,b)

def mayornumeroencontrado(mat):
    mayor=[0][0]
    xcoor=[0]
    ycoor=[0]
    tamaño=len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            if mat[ff][cc]> mayor:
                mayor= mat[ff][cc]
                xcoor = [ff]
                ycoor = [cc]

    return ycoor,xcoor


#PROGRAMA PRINCIPAL
n=int(input("Ingrese el tamaño de la matriz que desea:")) #Hago asi pq no especifica, creo.
matriz= []
for f in range(n):
    matriz.append([])
    for c in range(n):
        matriz[f].append(0)

rellenarmatriz(matriz)
imprimirmatriz(matriz)
print("La coordenada del mayor numero encontrado es: ", mayornumeroencontrado(matriz))
