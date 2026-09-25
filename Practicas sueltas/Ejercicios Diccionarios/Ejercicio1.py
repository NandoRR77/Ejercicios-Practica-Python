'''
Ejercicio 1: 
El inventario de frutas

Tienes un diccionario con el inventario actual de una tienda. Tu tarea es recorrer el 
diccionario y aumentar en 10 unidades el stock de cada una de las frutas directamente 
en la estructura original.

Estructura de datos:

frutas = {
    "manzanas": 5,
    "bananos": 12,
    "peras": 8
}
'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

frutas = {
    "manzanas": 5,
    "bananos": 12,
    "peras": 8
}
print(f'Frutas original: {frutas}')

for fruta, cantidad in frutas.items():
    frutas[fruta] = cantidad +10
print(f'Frutas con cantidad aumentada en 10: {frutas}')