#funcion
def sumarenteros(a,b):
    suma=0
    if a==b:
        return(a,b)
    elif a>b:
        while a!=b:
            suma= suma+b
            b=b+1
        suma=suma+a
    elif b>a:
        while b!=a:
            suma =suma +a
            a=a+1
        suma =suma +b
    return suma

x=int(input("Ingrese un numero entero:"))
y=int(input("Ingrese un numero entero:"))
resultado= sumarenteros(x,y)
print("El resultado de la suma es:", resultado)
