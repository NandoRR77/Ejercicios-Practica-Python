'''
4. Productos con stock disponible

Tienes una lista de productos en una bodega. 
Filtra los productos que tengan un stock mayor a 0.

Estructura:
python

inventario = [
    {"articulo": "Zapatos", "stock": 15},
    {"articulo": "Camisas", "stock": 0},
    {"articulo": "Pantalones", "stock": 8},
    {"articulo": "Gorras", "stock": 0}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

inventario = [
    {"articulo": "Zapatos", "stock": 15},
    {"articulo": "Camisas", "stock": 0},
    {"articulo": "Pantalones", "stock": 8},
    {"articulo": "Gorras", "stock": 0}
]

#Creo la nueva lista
en_stock = list(filter(lambda item: item["stock"] > 0, inventario))
#Este es un filtro con dos condiciones:
'''
en_stock = list(filter(lambda item: item["stock"] > 0 or item["articulo"] == "Camisas", inventario))
'''


#Imprimo los resultados
print(f'Lista con todos los artículos {inventario}')
print(f'\nLista artículos en stock {en_stock}')

#Imprimir cada elemento del diccionario con salto de linea
print("\nLista artículos en stock:", *en_stock, sep="\n")

