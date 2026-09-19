'''Ejercicio 4: Aplanar una matriz (Intermedio-Alto)
Reto: Tienes una lista que contiene otras listas de números 
(una matriz de 2D, por ejemplo: [[1, 2], [3, 4], [5, 6]]). 
Usa list comprehension para "aplanar" la estructura y obtener una sola 
lista continua con todos los números: [1, 2, 3, 4, 5, 6].
'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

matriz = [[1, 2], [3, 4], [5, 6]]
lista = []
for i in matriz:
    for j in i:
        lista.append(j)
print(lista)

lista2 = [j for i in matriz for j in i]
print(lista2)