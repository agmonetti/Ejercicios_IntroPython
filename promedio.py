#Funcion
def promediodiv (n):
    num=0
    contar=0
    x=0
    if n<0:
        n= -n 
    
    while num <n:
        if n%2==0:
            num=num+1
            if n%num==0:
                x=x+num
                contar= contar+1
    if contar !=0:          
        prom=(x*1/contar)
        return prom
    
    else:
        return 0

#Programa principal
entero=int(input("Ingresar un numero entero:"))
prome=promediodiv(entero)
print("Su promedio es:",prome)