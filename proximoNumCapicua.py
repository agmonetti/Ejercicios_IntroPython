"""
Desarrollar una función que reciba como parámetro un número entero positivo cualquie-ra y devuelva el próximo número capicúa.
Por ejemplo, si la función recibe 1024 debe devolver 1111.
Escribir también un programa para ingresar un número entero, verificar que sea positivo, invocar a la función y mostrar el resultado. """

#Un número es capicúa si se puede leer igual de derecha a izquierda que de izquierda a derecha

def buscar_invertido(num):
    numAux = num
    invertido = 0
    while numAux > 0:
        digito = numAux % 10
        invertido = invertido * 10 + digito
        numAux = numAux // 10
    return invertido


def capicu(numero):
    invertido = buscar_invertido(numero)
    while numero != invertido:
        numero = numero + 1
        invertido = buscar_invertido(numero)
        if numero == invertido:
            print("El sig num capicua es: ", numero)


#Programa Principal
n = int(input("Ingrese un numero: "))
while n < 10:
    print("El numero debe ser de al menos dos cifras")
    n = int(input("Ingrese un numero: "))
capicu(n)