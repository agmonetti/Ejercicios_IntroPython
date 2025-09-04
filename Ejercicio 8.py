sueldobasico=int(input("Ingrese el sueldo basico "))
antiguedad=int(input("Ingrese su antiguedad  "))
estadocivil=input("Ingrese su estado civil(c/s) ")

print()
if estadocivil =="s":
    gananciaantiguedad=sueldobasico+(sueldobasico*0.05)*antiguedad
    print("su estado civil es soltero")
elif estadocivil =="c":
    gananciaantiguedad=sueldobasico+(sueldobasico*0.07)*antiguedad
    print("su estado civil es casado")
    
sueldobruto=gananciaantiguedad+sueldobasico

jubilacion=sueldobruto*0.11
obrasocial=sueldobruto*0.03
sindicato=sueldobruto*0.03

sueldoneto=sueldobruto-jubilacion-obrasocial-sindicato

print("Su sueldo básico es de $", sueldobasico)
print("Cuenta con ", antiguedad, "años de antigüedad, que equivalen a $", gananciaantiguedad)
print("Su sueldo bruto es de $", sueldobruto)
print("Por jubilacion se le descuentan $", jubilacion)
print("Por obra social se le descuentan $", obrasocial)
print("Por sindicato se le descuentan $", sindicato)
print("Su sueldo neto es de $", sueldoneto)