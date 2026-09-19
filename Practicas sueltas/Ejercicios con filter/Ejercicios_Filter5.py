'''
5. Filtrar un diccionario de precios (Llave-Valor)

Tienes un diccionario con las tarifas de varios servicios. 
Filtra el diccionario usando .items() para conservar solo los 
servicios que cuesten 50 o menos.

Estructura:

python

servicios = {
    "Internet": 60,
    "Agua": 25,
    "Luz": 45,
    "Gas": 15,
    "Streaming": 55
}

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

servicios = {
    "Internet": 60,
    "Agua": 25,
    "Luz": 45,
    "Gas": 15,
    "Streaming": 55
}

#Creo la nueva lista
servicios_filtrados = dict(filter(lambda item: item[1] <= 50, servicios.items()))

#Solución método tradicional
'''servicios_filtrados = {}
for clave, valor in servicios.items():
    if valor <= 50:
        servicios_filtrados[clave] = valor
print(f'Nuevo diccionario {servicios_filtrados}')
'''

#Imprimo los resultados
print(f'Lista con todos los servicios {servicios}')
print(f'\nLista con los servicios que valen menos de 50 \n{servicios_filtrados}')


