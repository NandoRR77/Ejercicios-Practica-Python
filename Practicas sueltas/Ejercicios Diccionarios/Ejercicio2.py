'''
Ejercicio 2: Clasificador de números

Tienes una lista de números mixtos. 
Crea dos listas vacías: una llamada pares y otra llamada impares. 
Recorre la lista original con un bucle for e introduce cada número en su lista correspondiente.

Estructura de datos:

numeros = [14, 3, 8, 21, 5, 10, 33, 42]
'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

numeros = [14, 3, 8, 21, 5, 10, 33, 42]

print(f'Lista de números original: {numeros}')

numeros_pares = [i for i in numeros if i % 2 == 0]
numeros_impares = [i for i in numeros if i % 2 != 0]


print(f'Lista de números pares: {numeros_pares}')
print(f'Lista de números impares: {numeros_impares}')


#Solución con for
pares = []
impares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(f'Lista de números pares: {pares}')
print(f'Lista de números impares: {impares}')