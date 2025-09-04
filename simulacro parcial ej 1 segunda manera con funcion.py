#funcion
def porcentaje(cant,contar):
    porcentaje_total = (cant * 100) / (contar)
    return porcentaje_total

#programa principal
contar= 0
contar_adolescentes= 0
contar_adultos=0
contar_adultos_mayores=0
contar_niños=0
edad1=0
edad=int(input("Ingrese la edad de la persona"))

while edad != -1:
    
    if edad >0 and edad <=12:
        contar_niños=contar_niños + 1
        edad1=edad
        contar=contar +1
        edad=int(input("Ingrese la edad de la persona"))
        if edad== edad1:
            contar_niños=contar_niños -1
    
    elif edad >= 13 and edad <=20:
        contar_adolescentes= contar_adolescentes + 1
        edad1=edad
        contar= contar +1
        edad=int(input("Ingrese la edad de la persona"))
        if edad== edad1:
            contar_adolescentes= contar_adolescentes -1
    
    elif edad >= 21 and edad <= 69:
        contar_adultos=contar_adultos + 1
        edad1=edad
        contar= contar+1
        edad=int(input("Ingrese la edad de la persona"))
        if edad==edad1:
            contar_adultos=contar_adultos -1
    
    elif edad > 70:
        contar_adultos_mayores= contar_adultos_mayores + 1
        edad1=edad
        contar=contar +1 
        edad=int(input("Ingrese la edad de la persona"))
        if edad==edad1:
            contar_adultos_mayores= contar_adultos_mayores - 1
     
  
print("_Niños:" ,contar_niños,porcentaje(contar_niños,contar) ,"%")
print("_Adolescentes:" ,contar_adolescentes, porcentaje(contar_adolescentes, contar),"%")
print("_Adultos:", contar_adultos,porcentaje(contar_adultos,contar),"%")
print("_Adultos mayores:", contar_adultos_mayores,porcentaje(contar_adultos_mayores,contar),"%")
print("El segmento mas poblado es:",)