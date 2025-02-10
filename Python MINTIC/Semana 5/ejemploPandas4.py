#Crear y visualizar un arreglo unidimensional como una estructura de Series
import pandas as pd

datos = [1,2,3,4,5]
serie = pd.Series(datos)
print(type(datos))
print(type(serie))
print(serie)
print()

#Convertir un objeto Serie en un alista Python
print()
datos1 = [6,7,8,9,10]
serie1 = pd.Series(datos1)
print(type(datos1))
print(type(serie1))
print(serie1)
print()

lista = serie1.tolist() #con esto convierto a una lista
print(type(lista))
print(lista) 
print()

#Aplicar las operaciones aritméticas básicas sobre objetos Serie
print("Actividad 4")
serie2 = pd.Series([1,2,3,4,5])
serie3 = pd.Series([6,7,8,9,10])
print(serie2 + serie3)
print(serie2 - serie3)
print(serie2 * serie3)
print(serie2 / serie3)

#Usar operadores relacionales para comparar objetos serie
print(serie2 > serie3)
print(serie2 < serie3)
print(serie2 == serie3)
print(serie2 != serie3)