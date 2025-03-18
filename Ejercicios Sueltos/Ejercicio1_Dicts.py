'''
Ejercicio 1 - Crear un diccionario de frutas asi:
manzanas = 5
peras = 2
naranjas = 4

Imprimir en pantalla la cantidad de manzanas

'''

fruits = {
    'manzanas': 5,
    'peras': 2,
    'naranjas': 4}

print(f'La cantidad de manzanas es (método valor): {fruits['manzanas']}')
print(f'La cantidad de manzanas es (método get): {fruits.get('manzanas')}')

