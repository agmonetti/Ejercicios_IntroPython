#Una editorial determina el precio de un libro según la cantidad de páginas.

#El costo básico del libro es de $500, más $20,20 por págoma con ecuadernacio rustica.
#Si el numero de paginas supera las 300 la encuadernacion debe ser en tela, incrementa $200.
#Si el numero de paginas supera las 600 se hace un encuadernado especial, incrementa en $336.


libro=int(input("Ingresar la cantidad de paginas del libro:"))

if libro < 300:
    print("El libro cuesta: $520.20")

elif libro >= 600:
    print("El libro cuesta: $1036")
else:
    print("El libro cuesta $700")
    