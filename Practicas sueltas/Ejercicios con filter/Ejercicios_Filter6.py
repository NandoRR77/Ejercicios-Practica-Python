'''
6. Tienes una lista de estudiantes (diccionarios). 

Filtra la lista para conservar solo a los alumnos cuyo nombre comience con la letra "M".

Estructura de datos:

python

alumnos = [
    {"nombre": "Miguel", "curso": "A"},
    {"nombre": "Sofía", "curso": "B"},
    {"nombre": "Marta", "curso": "A"},
    {"nombre": "Alejandro", "curso": "C"},
    {"nombre": "Manolo", "curso": "B"}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

alumnos = [
    {"nombre": "Miguel", "curso": "A"},
    {"nombre": "Sofía", "curso": "B"},
    {"nombre": "Marta", "curso": "A"},
    {"nombre": "Alejandro", "curso": "C"},
    {"nombre": "Manolo", "curso": "B"}
]

#Creo la nueva lista
alumnos_filtrados = list(filter(lambda alumno: alumno['nombre'].startswith('M'), alumnos))

'''Solución método tradicional
alumnos_filtrados2 = []
for alumno in alumnos:
   if alumno['nombre'].startswith('M'):
       alumnos_filtrados2.append(alumno)
print(alumnos_filtrados2)
'''

#Imprimo los resultados
print(f'Lista con todos los alumnos{alumnos}')
print('Lista con los alumnos cuyo nombre comienza por M:', *alumnos_filtrados, sep="\n")


