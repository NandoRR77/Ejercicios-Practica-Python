import pandas as pd

s = pd.Series({"Matematicas":3.5 ,"Historia":4.5 ,"Economia": 3 ,"Programacion": 3.3 ,"Ingles":0},dtype="string") #diccionario convertida a serie
print(s)
print()
print(s[1:3]) #imprime desde Historia hasta economia. 
print()
print(s["Historia"]) #imprime el value de Historia
print()
print(s[["Historia"]]) #imprime la clave y value de Historia
print() 
print(s[["Historia","Ingles"]]) #imprime la clave y value de Historia e Ingles
print() 