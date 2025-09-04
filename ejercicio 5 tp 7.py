import random

lista= []
azar= random.randint(0,101)

    
for i in range(azar):
    azar= random.randint(0,101)
    lista.append(azar)
    
    
if lista == 0:
    print("La lista ha terminado")

print(lista)