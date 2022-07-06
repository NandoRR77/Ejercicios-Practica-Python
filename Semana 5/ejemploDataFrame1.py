import pandas as pd

#Convertir un diccionario Python en un objeto Series
print("Convertir un diccionario Python en un objeto Series")
dicc = {"A":10,"B":20,"C":30}
serie = pd.Series(dicc)
print(serie)
print(serie["A"]) #imprime el value del key A

#Convertir un arreglo Numpy en un objeto Series
print()
print("Convertir un arreglo Numpy en un objeto Series")
import numpy as np 

arreglo = np.array([2,3,4,5,6]) #creo el arreglo con Array porque le voy a dar los valores, sino, seria con arange
print(arreglo)
print()
serieArr = pd.Series(arreglo) #convierto el arrego en una serie
print(serieArr)
print()

#Cambiar el tipo de datos de un objeto Series
print()
print("Cambiar el tipo de datos de un objeto Series")
datos = pd.Series(["100","200","300","Sailor Moon","300.15","He-Man"])
datos = pd.to_numeric(datos, errors = "coerce") #Lo que no sea números los transforma en no definido NaN para que no salga error
print(datos)

#Obtener una columna de un objeto DataFrame como un objeto Series
print()
print("Obtener una columna de un objeto DataFrame como un objeto Series")
datosDic = {"A":[1,2,3,4,5], "B":[5,6,7,8,9], "C":[2,7,10,11,12]}
df = pd.DataFrame(data=datosDic) #con estos convierto el diccionario a un data frame
print(df)
print()
columna = df.iloc[:,1]#con esto imprimo la columna 1, o sea la B
print(columna)
print()

#Extraer una fila de un DataFrame como un objeto Series
print()
print("Extraer una fila de un DataFrame como un objeto Series")
fila = df.iloc[1,:]#con esto imprimo la fila 1, o sea 2,6,7
print(fila)
print()

print(df.iloc[3,1]) #imprime el elemento f3, c1 = 8
print()

print(df.iloc[:,0:2]) #imprime las columnas a y b
print()

