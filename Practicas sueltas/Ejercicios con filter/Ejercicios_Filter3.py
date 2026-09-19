'''
3. Empleados con sueldos altos

Tienes una lista de diccionarios con empleados. Filtra a aquellos cuyo salario sea 
estrictamente mayor a 3000.

Estructura:

empleados = [
    {"nombre": "Ana", "salario": 2500},
    {"nombre": "Luis", "salario": 4100},
    {"nombre": "María", "salario": 1800},
    {"nombre": "Pedro", "salario": 3500}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

empleados = [
    {"nombre": "Ana", "salario": 2500},
    {"nombre": "Luis", "salario": 4100},
    {"nombre": "María", "salario": 1800},
    {"nombre": "Pedro", "salario": 3500}
]

#Creo la nueva lista
salario_empleados = list(filter(lambda item: item['salario'] > 3000, empleados))


#Imprimo los resultados
print(f'Lista con todas las palabras {empleados}')
print(f'\nLista palabras con 5 letras {salario_empleados}')



