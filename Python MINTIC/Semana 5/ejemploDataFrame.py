import pandas as pd

#Convertir un objeto Series con múltiples listad en un único objeto Series
print("Convertir un objeto Series con múltiples listad en un único objeto Series")
datos = [["Colombia","Peru","Brasil","Argentina"],["Ecuador","Mexico"],["Chile"]] #Creo una lista con listas como elementos
serie = pd.Series(datos) #convierto la lista datos en serie
print(serie)
print()

serie = serie.apply(pd.Series) #con esto las listas que estaban como elementos los convierto a serie otra vez
print(serie)
print()

serie = serie.apply(pd.Series).stack() #con esto organizo los elementos en columna
print(serie)
print()

serie = serie.apply(pd.Series).stack().reset_index(drop=True) #con esto reseteo los indices para que me muestre solo 1 por elemento
print(serie)
print()


#Ordenar los valores de un objeto Series con el método sort_values
print("Ordenar los valores de un objeto Series con el método sort_values")
datosOrd=["1.1", "20", "30", "0.5", "Panda", "Java"]
serieOrd = pd.Series(datosOrd)
serieOrd = pd.Series(serieOrd).sort_values()
print(serieOrd)
print()


#Agregar datos a un objeto Series existente
print("Agregar datos a un objeto Series existente")
serieOrd = serieOrd.append(pd.Series(["JavaScript", "HTML"])).reset_index(drop=True)
print(serieOrd)
print()