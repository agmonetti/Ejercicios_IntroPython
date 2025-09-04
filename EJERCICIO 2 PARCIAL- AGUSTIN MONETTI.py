#Funcion
def promediodiv (n):
    num=0
    if n<0:
        print("El numero debe ser positivo")
    else:
        while num <n:
            if n%2==0:
                num= num+1
                if n%num == 0:
                    while num>=entero and num<=n:
                        num=num +entero
                        print(num*n/100)
                        
    return num  


#Programa principal

entero=int(input("Ingresar un numero entero"))
divisores = promediodiv(entero)
print((divisores-1)/5)