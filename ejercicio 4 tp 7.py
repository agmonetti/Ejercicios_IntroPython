import random

azar= 5
lista1= []
lista2= []
lista3= []
for i in range(azar):
    lista= random.randint(1,40)
    lista1.append(lista)
    
for i in range(azar):
    lista= random.randint(1,20)
    lista2.append(lista)

for i in range(len(lista1)):
    lista3.append(lista1[i]+lista2[i])

print(lista1)
print()
print(lista2)
print()
print(lista3)