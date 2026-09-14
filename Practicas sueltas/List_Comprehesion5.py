'''Ejercicio 5_2: Separador de palabras por frases
Imagina que tienes una lista que contiene varias frases cortas 
(un texto dividido por oraciones). 
Tu objetivo es "romper" esas frases y obtener una sola lista continua con todas 
las palabras sueltas.

frases = ["hola mundo", "python es genial", "me gusta programar"]
'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

frase = ["hola mundo", "python es genial", "me gusta programar"]
print(f'Frase original (lista de frases) {frase}')

#Método tradicional
oracion = []
for i in frase:
    for j in i.split():
        oracion.append(j)
print(f'Oración sin list comprehesion {oracion}')
        
#Con list comprehesion
oracion2 = [j for i in frase for j in i.split()] 
print(f'Oración con list comprehesion {oracion2}')