"""
1 pie =12 pulgadas
3 pies= 1 yarda
1 pulgada=2,54 cm
1 metro= 100 cm

"""
metro=int(input("Ingresar una medida en metros:"))
centimetro=print("La medida en centimetros es:" ,metro*100,"cm")
centimetro=int(metro*100)
pulgadas=print("La medida en pulgadas es:",centimetro/2.54, "pulgadas")
pulgadas=int(centimetro/2.54)
pie=print("La medida en pies es:", pulgadas/12,"pies")
pie=int(pulgadas/12)
yarda=print("La medida en yardas es:", pie/3,"yardas")
yarda=int(pie/3)
