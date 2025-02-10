import pandas as pd
import numpy as np 

#Obtener las primeras n filas de un objeto DataFrame
print("Obtener las primeras n filas de un objeto DataFrame")
nombre = ["Sebastian", "Alonso", "Edgar", "Helena", "Liceth", "Loraine", "Maria"]
puntaje = [11.5, 8, 15.5, 18, 22.3, 10, 11]
intentos = [1,2,1,3,4,5,2]
califico = ["si", "no", "no", "si", "si", "si", "si"]
indices = ["A", "B", "C", "D", "E", "F", "G"]
jugadores = {"NOMBRE": nombre, "PUNTAJE":puntaje, "INTENTOS":intentos, "CALIFICO":califico}
df = pd.DataFrame(data=jugadores, index=indices)
print(df)
print()
print(df.iloc[:3])

#Obtener las ultimas n filas de un objeto DataFrame
print()
print(df.iloc[-5:])


#Obtener los ejes y atributos (las filas y columnas) de un DataFrame
print("Obtener los ejes y atributos (las filas y columnas) de un DataFrame")
print()
print(df.axes)


#Seleccionar las filas y columnas específicas de un DataFrame
print("Seleccionar las filas y columnas específicas de un DataFrame")
print()
print(df.iloc[[1,4],[0,3]])


#Obtener el tamaño,la dimension y la forma de un objeto DataFrame
print("Obtener la dimension, el tamaño y la forma de un objeto DataFrame")
print()
print(df.size) #cantidad de elementos
print()
print(df.ndim) #Dataframe de 2 dimensiones
print()
print(df.shape) #7 filas X 4 columbas
print()  

 
#Obtener la cantidad de memoria ocupada por cada columna en un DataFrame
print("Obtener la cantidad de memoria ocupada por cada columna en un DataFrame")
print(df.memory_usage()) #Tamaño en bits
print()