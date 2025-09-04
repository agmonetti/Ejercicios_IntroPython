#Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa que pueda ingresar el importe
#de cada venta realizada. Para indicar que finalizó el día se ingresa -1.
#¿Cuál fue el monto total vendido y cuántas ventas se realizaron? El importe de cada venta realizada debe ser un valor positivo.

n=int(input("Ingresar el importe de cada venta e indicar -1 cuando finalizó el día:"))
suma= 0
contar= 0

while n != -1:
    if n < 0:
        print("El importe debe ser un valor positivo")
        
    suma= suma + n
    contar= contar + 1
    n=int(input("Ingresar el importe de cada venta e indicar -1 cuando finalizó el día:"))
    

print("El monto total es: ", suma)
print("El total de ventas es: ", contar)

