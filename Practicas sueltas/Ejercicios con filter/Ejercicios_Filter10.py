'''
10. Filtrar canales con transmisiones en vivo populares

Filtra la lista para quedarte con los canales actualmente en vivo ("en_vivo": True) 

Y ADEMÁS que sus espectadores superen el promedio de espectadores de toda la lista.

Estructura de datos:

canales = [
    {"canal": "GamerPro", "en_vivo": True, "espectadores": 1500},
    {"canal": "CookingTime", "en_vivo": False, "espectadores": 0},
    {"canal": "MusicVibes", "en_vivo": True, "espectadores": 400},
    {"canal": "TechTalk", "en_vivo": True, "espectadores": 2200},
    {"canal": "DevLife", "en_vivo": False, "espectadores": 0},
    {"canal": "ChessMaster", "en_vivo": True, "espectadores": 800}
]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

canales = [
    {"canal": "GamerPro", "en_vivo": True, "espectadores": 1500},
    {"canal": "CookingTime", "en_vivo": False, "espectadores": 0},
    {"canal": "MusicVibes", "en_vivo": True, "espectadores": 400},
    {"canal": "TechTalk", "en_vivo": True, "espectadores": 2200},
    {"canal": "DevLife", "en_vivo": False, "espectadores": 0},
    {"canal": "ChessMaster", "en_vivo": True, "espectadores": 800}
]

#Creo la nueva lista
#aprobaron = list(filter(lambda alumno: len(alumno["notas"]) > 0 and sum(alumno["notas"]) / len(alumno["notas"]) >= 8 ,clase ))
espect_filtrados = []

'''
#Solución tradicional
#Con este print llego a las notas de un alumno en específico
#print(clase[0]['notas'])


'''

#Imprimo los resultados
print(f'\nLista con todos los canales: \n{canales}')
print('\nLista con los alumnos con promedio mayor a 8', *espect_filtrados, sep="\n")
