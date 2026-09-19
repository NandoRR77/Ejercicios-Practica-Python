'''
8. Filtrar el carrito de compras de un usuario

Tienes la información de una sesión de usuario. El diccionario contiene sus datos y una 
lista de productos dentro de su carrito. Filtra la lista interna de carrito para obtener 
solo los productos que tengan un precio mayor o igual a 20.

Estructura de datos

usuario = {
    "username": "coder_girl",
    "carrito": [
        {"item": "Libro", "precio": 15},
        {"item": "Termo", "precio": 25},
        {"item": "Stickers", "precio": 5},
        {"item": "Mochila", "precio": 45}
    ]
}

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

usuario = {
    "username": "coder_girl",
    "carrito": [
        {"item": "Libro", "precio": 15},
        {"item": "Termo", "precio": 25},
        {"item": "Stickers", "precio": 5},
        {"item": "Mochila", "precio": 45}
    ]
}

#Creo la nueva lista
lista_filtrada = list(filter(lambda producto: producto['precio'] >= 20, usuario['carrito']))

'''
Solución tradicional
#con este print recorro las llaves del diccionario
print(usuario.keys())

#Con este print entro hasta la llave precio del diccionario interno
print(usuario["carrito"][0]["precio"])

#Paso del print anterior al bucle para saber que precio cumple la condición
lista_filtrada = []
for producto in usuario["carrito"]:
    if producto['precio'] >= 20:
        lista_filtrada.append(producto)
    else:
        continue
print(lista_filtrada)
'''

#Imprimo los resultados
print(f'\nLista con todos los items: \n{usuario}')
print('\nLista con los items con precio mayor a 20', *lista_filtrada, sep="\n")


