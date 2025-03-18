'''
Ejercicio 5 - Para diccionario de frutas retornar True si la clave 'manzanas' existe en el
diccionario o false si no
'''

fruits = {
    'manzanas': 5,
    'peras': 2,
    'naranjas': 4
    }

fruit = 'manzanas'
print(f'Diccionario inicial: {fruits}')
print(f'La fruta {fruit} existe en el diccionario?\n===>{fruit in fruits}')