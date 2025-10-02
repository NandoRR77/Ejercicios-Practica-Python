import sys
print(sys.path)


#Módulo expresiones regulares
import re
text = 'Mi número de telefono es 3003345998, el código del pais es 57, mi numero de la suerte es 9'

result = re.findall('[0-9]+', text)

print(result)


#Módulo tiempo
#Manejo de hora de la máquina
import time
timestamp = time.time()

local = time.localtime()

result = time.asctime(local)

print(timestamp)
print(result)


#Manejo de listas
#Contar la frecuencia de cada elemento de una lista
import collections

numbers = [1,1,1,2,2,2,3,4,5,5,5,5,21]
counter = collections.Counter(numbers)
print(counter)