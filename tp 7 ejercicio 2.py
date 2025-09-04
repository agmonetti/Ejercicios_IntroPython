import random

def lista_alazar(a, b):
    n= int(input("Inrese la cantidad de numeros que quiere"))
    lista =[]
    for i in range(n):
        c= random.randint(minimo,maximo)
        lista[i]=lista.append(c)
       
        
    return lista

minimo=int(input("Ingrese el valor minimo dentro del cual se va a generar la lista"))
maximo=int(input("Ingrese el valor maximo dentro del cual se va a generar la lista"))
mlista= lista_alazar(minimo,maximo)
print(mlista)