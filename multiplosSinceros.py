#Ejercicio 1

#programa principal


n=int(input("Ingrese un numero entero de una o mas cifras:"))
n_unacifra=int(input("Ingrese un numero entero de una sola cifra:"))
cifra=0
suma_digitos=0
while n_unacifra <0 and n_unacifra >9:
    print("El numero debe ser de una sola cifra")
    n_unacifra=int(input("Ingrese un numero entero de una sola cifra:"))

while n !=0:
    cifra= n%10
    n= n//10
    suma_digitos=suma_digitos+cifra

if suma_digitos== n_unacifra:
    print("Son multiplos sinceros" )
    
else:
    print("No son multiplos sinceros")
    
    
    

