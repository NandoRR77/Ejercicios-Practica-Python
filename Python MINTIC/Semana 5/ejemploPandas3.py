import pandas as pd

s = pd.Series((1,2,3,4,5,5,4,4,4,4,3,3)) #tupla convertida a serie

print(s.size) #muestra el tamaño de la serie
print(s.index) #muestra donde comienza, cantidad de elementos y saltos entre elementos
print(s.dtype) #imprime el tipo de dato de la serie