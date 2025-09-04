#Cada cliente que va al banco Express, indica su número de documento y aguarda a ser atendido,
#cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos.
#El banco desea saber quién fue el primer cliente atendido y quién fue el último.

n=int(input("Ingresar un numero de documento:"))
primero=0
ultimo=0

if n == -1:
    print("No se han ingresado personas hoy")
else:
    primero=n
    while n !=-1:
        ultimo=n
        n=int(input("Ingresar un numero de documento:"))

    print("El primer cliente ingresado fue:", primero)
    print("El ultimo cliente ingresado fue:", ultimo)
    