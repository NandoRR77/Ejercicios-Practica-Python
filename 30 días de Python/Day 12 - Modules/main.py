#Importar todo el módulo
import mymodule

print(mymodule.generate_full_name("Fernando", "Ramirez"))


#Importar solo una función del módulo y renommbrarla
from mymodule import sum_two_numbers as suma 

print(suma(7,12))


'''
##########################################################################################################################
Módulo de sistema operativo

Usando el módulo python os es posible realizar automáticamente muchas tareas del sistema operativo. 
El módulo OS en Python proporciona funciones para crear, cambiar el directorio de trabajo actual y 
eliminar un directorio (carpeta), obtener su contenido, cambiar e identificar el directorio actual.

# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()


##########################################################################################################################
Módulo Sys

El módulo sys proporciona funciones y variables utilizadas para manipular diferentes partes del entorno de tiempo de 
ejecución de Python. La función sys.argv devuelve una lista de argumentos de línea de comandos pasados a un script Python. 
El elemento en el índice 0 en esta lista es siempre el nombre del script, en el índice 1 es el argumento pasado desde la 
línea de comandos.

import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))


Algunos comandos útiles de sys:

# to exit sys
sys.exit()

# To know the largest integer variable it takes
sys.maxsize

# To know environment path
sys.path

# To know the version of python you are using
sys.version


##########################################################################################################################
Módulo de estadísticas

El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. 
Las funciones estadísticas populares que se definen en este módulo: media, mediana, modo, stdev, etc.

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3


##########################################################################################################################
Módulo de matemáticas

Módulo que contiene muchas operaciones matemáticas y constantes.

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
Ahora, hemos importado el módulo de matemáticas que contiene muchas funciones que pueden ayudarnos a realizar cálculos 
matemáticos. Para comprobar qué funciones tiene el módulo, podemos usar help(math) o dir(math). Esto mostrará las funciones disponibles en el módulo. Si queremos importar solo una función específica del módulo, la importamos de la siguiente manera:

from math import pi
print(pi)
También es posible importar múltiples funciones a la vez

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
Pero si queremos importar todas las funciones en el módulo de matemáticas, podemos usar *.

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
Cuando importamos, también podemos renombrar el nombre de la función.

from math import pi as  PI
print(PI) # 3.141592653589793


##########################################################################################################################
Módulo de cadena

Un módulo de cadena es un módulo útil para muchos propósitos. El siguiente ejemplo muestra algún uso del módulo de cadenas.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


##########################################################################################################################
Módulo aleatorio

A estas alturas ya está familiarizado con la importación de módulos. Hagamos una importación más para familiarizarnos mucho 
con ella. Vamos a importar un módulo aleatorio que nos da un número aleatorio entre 0 y 0,9999... 
El módulo aleatorio tiene muchas funciones, pero en esta sección solo usaremos random y randint.

from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
🌕 Estás yendo lejos. ¡Sigue adelante! Acabas de completar los desafíos del día 12 y estás a 12 pasos de cabeza en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y músculos.


'''