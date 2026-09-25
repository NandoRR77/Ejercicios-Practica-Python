'''
Ejercicio 3: Añadir el impuesto a los productos

Tienes una lista de productos (diccionarios). Recorre la lista y, utilizando un bucle for, 
agrégale una nueva clave llamada "precio_con_iva" a cada producto. 
El valor debe ser el precio original multiplicado por 1.19 (el 19% de IVA).

Estructura de datos:

productos = [
    {"nombre": "Camiseta", "precio": 20},
    {"nombre": "Pantalón", "precio": 40},
    {"nombre": "Zapatos", "precio": 60}
]
'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

productos = [
    {"nombre": "Camiseta", "precio": 20},
    {"nombre": "Pantalón", "precio": 40},
    {"nombre": "Zapatos", "precio": 60}
]

#Solución con for
for producto in productos:
    producto['precio_con_iva'] = round(float(producto["precio"] * 1.19),2)
print('Nuevo diccionario precios con IVA: ', *productos, sep='\n')
