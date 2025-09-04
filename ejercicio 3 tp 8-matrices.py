"""Ingresar por teclado la cantidad de filas y de columnas de una matriz.
Generarla con valores al azar comprendidos entre a y b.
Mostrar la suma de los valores ubicados sobre la diagonal principal"""

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

def sumadiagonalprincipal(fil,col,matriz):
    total = 0
    for ff in range(fil):
        for cc in range(ff, col):
            total = total + matriz[ff][cc]
    return total

#PROGRAMA PRINCIPAL
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))
matriz= []
for f in range(filas):
    matriz.append([])
    for c in range(columnas):
        matriz[f].append(0)


rellenarmatriz(filas,columnas,matriz)
imprimirmatriz(matriz)
print("La suma de la diagonal principal es: ",sumadiagonalprincipal(filas,columnas,matriz))
