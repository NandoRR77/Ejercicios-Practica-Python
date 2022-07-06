'''Escribir un programa que pregunte al usuario por las ventas de un rango de años
y muestre por pantalla una serie con los datos de las ventas indexadas por los años, 
antes y despues de aplicarles un descuento del 10%'''

import pandas as pd

inicio = int(input("Por favor ingrese el año inicial de las ventas: "))
fin = int(input("Por favor ingrese el año final de las ventas: "))
ventas = {}

for i in range (inicio,fin+1):
    ventas[i] = float(input(f"Por favor ingrese las ventas de {i}: "))

ventas = pd.Series(ventas)
print()
print("Ventas por año \n")
print()
print(f"ventas con descuento \n {ventas * 0.9}")