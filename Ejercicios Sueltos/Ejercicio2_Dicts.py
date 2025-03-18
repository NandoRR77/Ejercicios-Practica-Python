'''
Ejercicio 2 - Agregar al diccionario de frutas los siguientes elementos:
bananas = 5
mangos = 6
uvas = 3

'''

fruits = {
    'manzanas': 5,
    'peras': 2,
    'naranjas': 4
    }

print(f'Diccionario inicial: {fruits}')


###Agregar valores
#Método pasando la clave y el valor
fruits['bananas'] = 5

print(f'Elemento agregado a método clave y valor{fruits}')

#Método setdefault()
fruits.setdefault('mangos', 6)
print(f'Elemento agregado a método setdefault(){fruits}') 

#Método update()
fruits.update({'uvas': 3})
print(f'Elemento agregado a método update(){fruits}') 



