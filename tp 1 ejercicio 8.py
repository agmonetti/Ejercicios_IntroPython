"""
Un banco necesita un programa que lea una cantidad de dinero
que desea retirare imprima a cuántos billetes equivale,
considerando que existen billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas de $10, $5, $2 y $1
Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""
dineroinicial=int(input("Ingresar la cantidad que desea retirar: $"))
billeteDeMil=dineroinicial//1000
restodemil=billeteDeMil%1000

print=("Billetes de mil retirados: $")