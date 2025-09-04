def cuantos_kilos(ingre1):
    ingre1 = ingre1 * 1000
    print("En total son", ingre1,"gramos")
    return ingre1

def hacer_torta(ingre1, ingre1necesario,ingre2, ingre2necesario,ingre3,ingre3necesario,comida_hecha):
    while(ingre1>=ingre1necesario and ingre2>=ingre2necesario and ingre3>=ingre3necesario):
        comida_hecha = comida_hecha+1
        ingre1 = ingre1-ingre1necesario
        ingre2 = ingre2-ingre2necesario
        ingre3 = ingre3-ingre3necesario
    return comida_hecha

def ingre_que_restan(ingre1, ingre1necesario,):
    while(ingre1>=ingre1necesario):
        ingre1 = ingre1 - ingre1necesario
    return ingre1

print("Bienvenido a la fabrica de chocolate")
print("-------------------------")
print("Recuerde ingresar en KG")

chocotorta = 0
dulce_de_leche_necesario = 400
galletitas_necesario = 500
queso_crema_necesario = 180
dulce_de_leche_cantidad = int(input("Cuanto kilos de leche tenes?"))
galletitas_cantidad = int(input("Cuantos kilos de galletitas tenes?"))
queso_crema_cantidad = int(input("Cuantos kilos queso crema tenes"))

dulce_de_leche_cantidad=cuantos_kilos(dulce_de_leche_cantidad)
galletitas_cantidad=cuantos_kilos(galletitas_cantidad)
queso_crema_cantidad=cuantos_kilos(queso_crema_cantidad)

chocotorta = hacer_torta(dulce_de_leche_cantidad,dulce_de_leche_necesario,galletitas_cantidad,galletitas_necesario,
              queso_crema_cantidad,queso_crema_necesario,chocotorta)
print("Se hicieron", chocotorta, "chocotortas")

dulce_de_leche_cantidad=ingre_que_restan(dulce_de_leche_cantidad,dulce_de_leche_necesario)
print("Le quedo", dulce_de_leche_cantidad, "gramos de dulce de leche")

galletitas_cantidad = ingre_que_restan(galletitas_cantidad,galletitas_necesario)
print("Le quedo", galletitas_cantidad, "gramos de dulce de galletitas")

queso_crema_cantidad = ingre_que_restan(queso_crema_cantidad,queso_crema_necesario)
print("Le quedo", queso_crema_cantidad, "gramos de queso crema")