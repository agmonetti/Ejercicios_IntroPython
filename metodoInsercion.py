lista = [4,2,9,1,0] # METODO SELECCION

largo=len(lista)
for i in range (largo-1):
    minimo = i
    for j in range (i + 1, largo):
        if lista[j] < lista[minimo]:
            minimo= j
            aux= lista[minimo]
            lista[minimo]=lista[i]
            lista[i]= aux
        
print(lista)

lista2 = [6,3,8,2,4] # METODO INSERCION
for i in range (1,len(lista2)):            #RECORRER LA LISTA
    aux = lista[i]
    maximo = i
    while maximo > 0 and lista2[maximo - 1] > aux:    #COMPARAR EL VALOR SELECCIONADO CON TODOS LOS ANTERIORES
        lista2[maximo] = lista2[maximo -1]        #INSERTAR EL VALOR DONDE CORRESPONDA
        maximo= maximo - 1
        lista2[maximo]= aux

print(lista2)

lista3 = [2,3,8,4,9]     #METODO BURBUJEO
for i in range(len(lista3)-1):
    for j in range(len(lista3)-1):
        if lista3[j] > lista3[j+1]:
            aux=lista3[j]
            lista3[j]= lista3[j+1]
            lista3[j+1]= aux
            
print(lista3)
            




