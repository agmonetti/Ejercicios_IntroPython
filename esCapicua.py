def escapicua1(lista):
    izq = 0
    der = len(lista) - 1
    while izq<der and lista[izq]==lista[der]:
        izq = izq + 1
        der = der - 1
    if izq>=der:
        return True
    else:
        return False

def escapicua2(lista):
    izq = 0
    der = len(lista) - 1
    capicua = True
    while izq<der and capicua:
        if lista[izq]!=lista[der]:
            capicua = False
        izq = izq + 1
        der = der - 1
    return capicua
