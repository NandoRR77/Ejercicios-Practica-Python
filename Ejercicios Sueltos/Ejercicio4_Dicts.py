'''
Ejercicio 4 - Para diccionario de frutas retornar dos listas, la primera todas las claves del 
diccionario y la segunda lista los valores
'''

fruits = {
    'manzanas': 5,
    'peras': 2,
    'naranjas': 4
    }

print(f'Diccionario inicial: {fruits}')

keys = fruits.keys()
print(f'Lista de claves: {list(keys)}')

values = fruits.values()
print(f'Lista de claves: {list(values)}')