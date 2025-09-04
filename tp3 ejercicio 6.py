#Una remiseria requiere un sistema que calcule el precio de un viaje a partir de la
#cantidad de KM que desea recorrer el usuario.

#Tarifa:
#Viaje minimo $50.
#Si recorre entre 0 y 10km: $20/km.
#Si recorre 10km o mas: $15/km.

km=int(input("Ingresar la cantidad de kilometros que desea recorrer:"))

if km >0 and km <10:
    print("El viaje cuesta:" , km*20+50)
if km >= 10:
    print("El viaje cuesta:" , km*15+50)
    

 
