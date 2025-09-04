a=int(input("Ingresar los años de antiguedad del empleado ó -1 para finalizar"))
contar1=0
contar2=0
contar3=0
contar4=0
contar=0
menor=a
mayor=a

while a != -1:
    if a<menor:
        menor=a
    if a>mayor:
        mayor=a
    
    if a>= 1 and a<= 10:
        contar=contar + 1
        contar1= contar1+1
        print("El empleado pertenece al Nivel 1")
        a=int(input("Ingresar los años de antiguedad del empleado ó -1 para finalizar"))
        
    elif a>= 11 and a<= 20:
        contar=contar+ 1
        contar2=contar2+ 1
        print("El empleado pertenece al nivel 2")
        a=int(input("Ingresar los años de antiguedad del empleado ó -1 para finalizar"))
        
    elif a>= 21 and a>=30 :
        contar=contar+1
        contar4=contar4 +1
        print("El empleado pertenece al nivel 3 y lleva mas de 30 años de antiguedad")
        a=int(input("Ingresar los años de antiguedad del empleado ó -1 para finalizar"))
    elif a>=21:
        contar=contar+1
        contar3=contar3 +1
        print("El empleado pertenece al nivel 3")
        a=int(input("Ingresar los años de antiguedad del empleado ó -1 para finalizar"))
   
print("El total de empleados en la empresa es de:", contar)
print("Pertenecen",contar1,"empleados en el Nivel 1")
print("Pertenecen",contar2,"empleados en el nivel 2")
print("Pertenecen",contar3+contar4,"empleados en el nivel 3")
print("El porcentaje que forma parte de la empresa por mas de 30 años es de",contar4*100/contar)
print("El empleado mas antiguo es:", mayor)
print("El empleado mas joven en relacion de antiguedad es:",menor)
    