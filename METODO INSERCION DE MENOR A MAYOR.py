lista2 = [6,3,8,2,4] # METODO INSERCION
for i in range (1,len(lista2)):
    aux = lista2[i]
    j = i
    while j < 0 and lista2 [j - 1] < aux:
        lista2[j] = lista2 [j-1]
        j= j - 1
        lista2[j]= aux

print(lista2)