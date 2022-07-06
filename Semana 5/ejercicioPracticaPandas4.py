'''Escribir un programa que genere y muestre por pantalla un DataFrame 
con los datos de la tabla'''

import pandas as pd

mes=["Enero", "Febrero", "Marzo", "Abril"]
ventas=[]
gastos=[]

for i in mes:
    ventas.append(float(input(f"Ingrese el valor de las ventas del mes {i}: ")))
    gastos.append(float(input(f"Ingrese el valor de los gastos del mes {i}: ")))
    
datosdicc = {"Ventas": ventas, "Gastos":gastos}
contabilidad = pd.DataFrame(datosdicc, columns=["Ventas","Gastos"], index=mes)
print(contabilidad)