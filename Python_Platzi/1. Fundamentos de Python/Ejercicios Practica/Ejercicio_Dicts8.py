'''
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista 
de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
'''

compras = {}
continuar = True
total_compras = 0

while continuar:
    clave = input('Ingrese artículo: ')
    valor = float(input(f'Ingrese valor del articulo {clave}: $ '))
    compras[clave] = valor
    total_compras += valor
    continuar = input('Desea agregar mas artículos (S/N)?: ').upper()
    if continuar  == 'S':
        continue
    else:
        break
    
print('Lista de la compra')
for clave, valor in compras.items():
    print(clave, '\t' , valor)
print('Total:\t' , total_compras )