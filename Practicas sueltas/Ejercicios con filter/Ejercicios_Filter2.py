'''
2. Filtrar palabras cortas
Tienes una lista de palabras. Filtra y conserva únicamente las que tengan menos de 5 letras.

Estructura:

palabras = ["sol", "computadora", "gato", "elefante", "mar", "azul"]

'''

#Para limpiar la terminal en cada ejecución
from os import system
if system("clear") != 0: system("cls")

palabras = ["sol", "computadora", "gato", "elefante", "mar", "azul"]

#Creo la nueva lista
palabras_filtradas = list(filter(lambda x: len(x) <= 5, palabras))



#Imprimo los resultados
print(f'Lista con todas las palabras {palabras}')
print(f'\nLista palabras con 5 letras {palabras_filtradas}')



