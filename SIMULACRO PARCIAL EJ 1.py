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
     
mayor=contar_niños     
print("_Niños:" ,contar_niños,contar_niños*100/contar ,"%")
print("_Adolescentes:" ,contar_adolescentes, contar_adolescentes*100/contar,"%")
print("_Adultos:", contar_adultos,contar_adultos*100/contar,"%")
print("_Adultos mayores:", contar_adultos_mayores,contar_adultos_mayores*100/contar,"%")
print("El segmento mas poblado es:")
if contar_adolescentes>mayor:
    mayor=contar_adolescentes
if contar_adultos>mayor:
    mayor=contar_adultos
if contar_adultos_mayores>mayor:
    mayor=contar_adultos_mayores
print("El segmento mas poblado es")
if mayor==contar_niños:
    print("Niños")
elif mayor==contar_adolescentes:
    print("Adolescentes")
elif mayor==contar_adultos:
    print("Adultos")
elif mayor== contar_adultos_mayores:
    print("Adultos mayores")
