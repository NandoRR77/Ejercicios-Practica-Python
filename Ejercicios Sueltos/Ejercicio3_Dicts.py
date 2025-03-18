'''
Ejercicio 3 - Eliminar del diccionario de frutas el par clave-valor correspondiente
a peras
'''

fruits = {
    'manzanas': 5,
    'peras': 2,
    'naranjas': 4
    }

print(f'Diccionario inicial: {fruits}')


#Eliminando peras
fruits.pop('peras')
print(f'Diccionario final {fruits}')
