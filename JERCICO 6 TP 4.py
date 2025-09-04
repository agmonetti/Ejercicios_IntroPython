#Ingresar números, hasta que la suma de los números pares supere 100. Mostrar Cuántos números en total se ingresaron.

n=int(input("Ingresar un numero entero:"))
sumapar= 0
cont= 1

while sumapar <100:
    cont= cont + 1
    
    if n%2 == 0:
        sumapar=sumapar + n
        n=int(input("Ingresar un numero entero"))
        
print( "Se ingresaron", cont, "numeros")


        


        
    

        
       
    
    
    
        
        
