'''Ejercicio 6: El Filtro de Matriz Impar
Tienes una matriz (lista de listas) con números variados:
matriz_numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Tu reto: Crea una list comprehension que "aplane" 
la matriz (como ya aprendiste a hacer), pero que solo conserve los números 
impares.

Resultado esperado: [1, 3, 5, 7, 9]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

matriz_numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Matriz original 2D {matriz_numeros}')

matriz_impares = []
for i in matriz_numeros:
    for j in i:
        if j % 2 != 0:
            matriz_impares.append(j)
        else:
            continue
print(f'Matriz impares {matriz_impares}')

#Con list comprehesion
matriz_impares2 =[j for i in matriz_numeros for j in i if j % 2 != 0]
print(f'Oración con list comprehesion {matriz_impares2}')

