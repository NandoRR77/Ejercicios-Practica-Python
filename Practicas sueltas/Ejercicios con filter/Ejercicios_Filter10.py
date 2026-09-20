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
#Defino la variable para el promedio global
prom_global = 0

#Calculo el total de espectadores con un list comprehesion. Sumando solo los espectadores y usando
#canal como iterador en canales
total_espectadores = sum([canal["espectadores"] for canal in canales])

#Calculo el promedio global con la variable total espectadores y la longitud del diccionario canales
prom_global = (total_espectadores / len(canales))

#print(f'Total espectadores con list comprehesion: {total_espectadores2}')
#print(f'Promedio espectadores: {prom_global:.2f}')

#Creo el filter con las dos condiciones dadas: canales en vivo y canal con espectadores superiores al promedio global
espect_filtrados = list(filter(lambda canal: canal["en_vivo"] and canal["espectadores"] > prom_global, canales))


'''
#Solución tradicional
#Con este print llego a las notas de un alumno en específico
print(canales[0]["espectadores"])

prom_global = 0
total_espectadores2 = 0

for canal in canales:
    total_espectadores2 += canal["espectadores"]
prom_global = total_espectadores2 / len(canales)

for canal in canales:
    if canal["en_vivo"] and canal["espectadores"] > prom_global:
        print(canal)
'''

#Imprimo los resultados
print('\nLista con todos los canales:', *canales, sep="\n")
print('\nLista con los canales en vivo y con promedio de espectadores mayor al promedio global:', *espect_filtrados, sep="\n")
