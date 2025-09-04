#Se desea analizar cuántos autos circulan con patente que tiene numeración par y cuántos con numeración impar en un día.
#Le solicitan escribir un algoritmo que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1
#e informar cuántas se ingresaron con numeración par y cuántas con numeración impar.

patente=int(input("Ingresar la terminarcion de la patente, entre 0 y 9 , hasta ingresar -1:"))
contar1= 0
contar2= 0

while patente >= 0 and patente <=9 :
    
    if patente%2 == 0:
        contar1= contar1 + 1
        patente=int(input("Ingresar la terminarcion de la patente, entre 0 y 9 , hasta ingresar -1:"))
    else:
        contar2= contar2 + 1
        patente=int(input("Ingresar la terminarcion de la patente, entre 0 y 9 , hasta ingresar -1:"))
        
print("Ingrsaron:" , contar1, "con numeracion par")
print("Ingresaron:", contar2,"con numeracion inpar")
