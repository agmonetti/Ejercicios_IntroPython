lista = [4,2,9,1,0]

largo=len(lista)
for i in range (largo-1):               #COMO ORDENAR DE MENOR A MAYOR CON METODO SELECCION
    menor = i
    for j in range (i + 1, largo):
        if lista[j] < lista[menor]:
            menor= j
            aux= lista[menor]
            lista[menor]=lista[i]
            lista[i]= aux
        

lista2 = [6,3,8,2,4]
lista3 = [2,3,8,4,9]

print(lista)
