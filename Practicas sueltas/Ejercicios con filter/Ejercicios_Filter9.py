'''
9. Filtrar alumnos por promedio de notas

Filtra la lista para dejar solo a los alumnos cuyo promedio de notas sea mayor o igual a 8.

Estructura de datos:

clase = [
    {"nombre": "Lucía", "notas": [9, 8, 10, 7]},
    {"nombre": "Jorge", "notas": [5, 6, 7, 5]},
    {"nombre": "Elena", "notas": [8, 9, 8, 9]},
    {"nombre": "Pablo", "notas": []}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

clase = [
    {"nombre": "Lucía", "notas": [9, 8, 10, 7]},
    {"nombre": "Jorge", "notas": [5, 6, 7, 5]},
    {"nombre": "Elena", "notas": [8, 9, 8, 9]},
    {"nombre": "Pablo", "notas": []}
]

#Creo la nueva lista
aprobaron = list(filter(lambda alumno: len(alumno["notas"]) > 0 and sum(alumno["notas"]) / len(alumno["notas"]) >= 8 ,clase ))

'''
#Solución tradicional
#Con este print llego a las notas de un alumno en específico
#print(clase[0]['notas'])

prom_notas = 0
for alumno in clase:
    if len(alumno['notas']) > 0:
        prom_notas =  sum(alumno["notas"]) / len(alumno["notas"])
        #print({prom_notas})
        if prom_notas >= 8:
            print(f'El almuno {alumno["nombre"]}, con promedio {prom_notas}, aprueba!')
        else:
            print(f'El almuno {alumno["nombre"]}, con promedio {prom_notas}, NO aprueba!')
    else:
        prom_notas = 0
        print(f'El almuno {alumno["nombre"]}, con promedio {prom_notas}, NO aprueba porque no tiene notas registradas!')
'''

#Imprimo los resultados
print(f'\nLista con todos los alumnos: \n{clase}')
print('\nLista con los alumnos con promedio mayor a 8', *aprobaron, sep="\n")
