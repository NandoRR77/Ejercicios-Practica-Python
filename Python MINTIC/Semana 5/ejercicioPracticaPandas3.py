'''Escribir una funcion que reciba un diccionario con las notas de los alumnos
en curso en un curso y devuelva una serie con las notas de los alumnos aprobados
ordenadas de mayor a menor'''

import pandas as pd

notas = {}
while True:
    nombre = input(f"Ingrese el nombre del alumno: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    notas[nombre] = nota
    opcion = input(f"Desea continuar S/N: ")
    if opcion.upper()!= "S":
        break

def estadisticasNotas(notas):
    notas = pd.Series(notas)
    return notas[notas>3.0].sort_values(ascending=False) #ordenar de mayor a menor solo las aprobadas

print()
print("Los estudiantes aprobados son: \n")
print(estadisticasNotas(notas))