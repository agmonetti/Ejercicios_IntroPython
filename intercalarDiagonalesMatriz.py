"""
Toda matriz cuadrada posee dos diagonales. La principal, que se extiende desde la esquina superioi izq hasta la
inferior derecha, y la secundaria, que va desde la esquina superior derecha hasta la inferior izq.

Desarrollar un programa para leer un numero entero positivo N y generar una matriz cuadrada NxN con numeros al azar
entre 1 y 9. Luego se solicita intercambiar sus diagonales principal y secundaria.
Imprimir la matriz antes y despues del proceso

 """
import random

def imprimirmatriz(mat):
    tamaño = len(mat)
    for ff in range(tamaño):
        for cc in range(tamaño):
            print(mat[ff][cc], end=" ")
        print()

def rellenarmatriz(numero,mat):
    for ff in range(numero):
        for cc in range(numero):
            mat[ff][cc] = random.randint(1,9)

#programa principal

N=int(input("Ingrese un numero entero positivo: "))
if N < 0:
    print("!Error¡  --> Debe ingresar un numero positivo")
    print("")
    N = int(input("Ingrese un numero entero positivo: "))

else:
    matriz= []
    for f in range(N):
        matriz.append([])
        for c in range(N):
            matriz[f].append(0)

rellenarmatriz(N,matriz)
imprimirmatriz(matriz)
print("")

print("la diagonal principal: ")
lista=[]
for fff in range(len(matriz)):
    for ccc in range(fff,(len(matriz))):
        lista.append(matriz[fff][ccc])

print(lista)
print("")

print("la diagonal secundaria:")

lista1=[]
suma=0
tamaño=len(matriz)
for fi in range(tamaño):
    for co in range(tamaño -1 ):
        suma=suma +(matriz[fi][co])
        lista1.append(matriz[fi][co])
        suma= suma -1

print(lista1)
print("")
print("La matriz intercambiada es:")

