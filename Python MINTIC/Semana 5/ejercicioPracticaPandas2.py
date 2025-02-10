'''Escribir una funcion que reciba un diccionario con las notas de los alumnos
en curso en un examen y devuelva una serie con la nota mínima, meida y la desviación
típica '''

import pandas as pd

notas = {"Juan":0, "Sebastian":0, "Franklin":0, "Michael":0, "Helena":0, "Loraine":0}

for keys in notas:
    notas[keys] = float(input(f"Digite la nota del estudiante {keys}: "))

print(notas)

def estadisticasNotas(notas):
    notas = pd.Series(notas)
    estadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index = ["Nota mínima", "Nota máxima", "Nota promedio", "Desviación típ¡ca"])
    return(estadisticos)

print(estadisticasNotas(notas))