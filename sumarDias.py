n=int(input("Ingrese la cantidad de dias que quiere sumar a la fecha de hoy:"))
d=12
m=5
a=2021
#1-3-5-7-8-10-12
while d+n <= 31 and m== 2 and m==4 and m== 6 and m==9 and m==11:
    d= d+1
if m> 31:
    m=m+1
    
print("La fecha de hoy es",d,"/",m,"/",a)
print("La fecha que quiero llegar es:",d,"/",m,"/",a)
