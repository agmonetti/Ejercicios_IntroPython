lista3 = [2,3,8,4,9]     #METODO BURBUJEO

for i in range(1,len(lista3)):
    for j in range(0,len(lista3)-1):
        if lista3[j+1] < lista3[j]:
            aux=lista3[j]
            lista3[j]= lista3[j+1]
            lista3[j+1]= aux
            
print(lista3)
            