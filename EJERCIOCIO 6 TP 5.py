dia=0
mes=1
año=2021

while dia <= 31:
    dia= dia + 1
    print("Dia" , dia , "del mes" ,mes)
    
    if dia > 31 and mes < 12:
        mes= mes + 1
        dia= 0
        dia= dia + 1
        print("Dia", dia, "del mes", mes)
    
