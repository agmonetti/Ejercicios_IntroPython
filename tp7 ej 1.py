def leernumero(a,b):
    n=int(input("Ingrese un numero entero o -1 para terminar"))
    while (n < a or n>b) and n != -1:
        print("El numero debe estar entre", a, "y", b)
        n=int(input("Ingrese un numero entero o -1 para terminar"))
    return n

def cargarlista(a,b):
    lista= []
    n = leernumero(a,b)
    while n != -1:
        lista.append(n)
        n = leernumero(a,b)
    return lista

def sumarlista(lista):
    total=0
    for k in range(len(lista)):
        total= total+ lista[k]
    return total
        
#Programa principal

minimo=int(input("Ingrese el valor minimo permitido"))
maximo= int(input("Ingrese el valor maximo permitido"))
print()
milista= cargarlista(minimo,maximo)
print(milista)

suma= sumarlista(milista)
print("La suma de la lista es",suma)