'''
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas 
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre 
por pantalla el precio de ese número de kilos de fruta. 
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	    Precio
Plátano	    1.35
Manzana	    0.80
Pera	    0.85
Naranja	    0.70
'''

fruits = {
    'Plátano' : 1.35,
    'Manzana' : 0.80,
    'Pera' : 0.85,
    'Naranja': 0.70
}

fruit = input('Por favor ingrese una fruta: \n')
cant = 0

if fruit in fruits:
    cant = int(input('Por favor ingrese la cantidad de kilos a comprar: \n'))
    total = fruits[fruit] * cant
    print(f'El valor de {cant} kgs de {fruit} es: ${total}')
else:
    print(f'La fruta {fruit} no existe en la bd')