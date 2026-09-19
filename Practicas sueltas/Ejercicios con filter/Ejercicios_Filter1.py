'''
1. Filtrar números negativos
Tienes una lista de temperaturas. Quédate solo con las que estén por 
debajo de 0 grados.

Estructura:

temperaturas = [12, -3, 5, 0, -1, -8, 22, -15]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

temperaturas = [12, -3, 5, 0, -1, -8, 22, -15]

#Creo la nueva lista
bajo_cero = list(filter(lambda x: x < 0, temperaturas))



#Imprimo los resultados
print(f'Lista con todas las temperaturas {temperaturas}')
print(f'\nLista temperaturas bajo cero {bajo_cero}')



