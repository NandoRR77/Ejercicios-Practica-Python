'''
7. Tareas pendientes de alta prioridad

Tienes una lista de tareas. Debes filtrar aquellas que cumplan dos condiciones al mismo tiempo: 
que su estado sea "Pendiente" Y que su prioridad sea "Alta".

Estructura de datos:

tareas = [
    {"titulo": "Enviar informe", "estado": "Pendiente", "prioridad": "Alta"},
    {"titulo": "Comprar café", "estado": "Pendiente", "prioridad": "Baja"},
    {"titulo": "Llamar al cliente", "estado": "Completado", "prioridad": "Alta"},
    {"titulo": "Corregir bug", "estado": "Pendiente", "prioridad": "Alta"}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

tareas = [
    {"titulo": "Enviar informe", "estado": "Pendiente", "prioridad": "Alta"},
    {"titulo": "Comprar café", "estado": "Pendiente", "prioridad": "Baja"},
    {"titulo": "Llamar al cliente", "estado": "Completado", "prioridad": "Alta"},
    {"titulo": "Corregir bug", "estado": "Pendiente", "prioridad": "Alta"}
]

#Creo la nueva lista
pendientes = list(filter(lambda x: x['estado'] == 'Pendiente' and x['prioridad'] == 'Alta', tareas))


#Solución método tradicional
print(f'\nSolución con método tradicional')

pendientes2 = []
for tarea in tareas:
    if tarea['estado'] == 'Pendiente' and tarea['prioridad'] == 'Alta':
        pendientes2.append(tarea)
print('Lista de resultado con solución tradicional\n', *pendientes2, sep="\n")

#Imprimo los resultados
print(f'\nLista con todas las tareas {tareas}')
print('\nLista con los pendientes de prioridad alta', *pendientes, sep="\n")


