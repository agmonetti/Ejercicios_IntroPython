#funcion
def recibirtitulo(titulo,asterisco):
    print("*" * asterisco)
    print(titulo)
    print("*" * asterisco)

#programa principal

title= input("Ingrese el titulo:")
asteriscos= int(input("Ingrese el numero:"))
recibirtitulo(title,asteriscos)
