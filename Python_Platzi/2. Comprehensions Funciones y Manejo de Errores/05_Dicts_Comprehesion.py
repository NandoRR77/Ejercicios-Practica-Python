'''
syntaxis = {key:value for var in iterable}


dict = {}

for i in range (1,11):
    dict[i] = i * 2
    
print(dict)

#Con Dict comprehesion

dict_v2 = { i:i * 2 for i in range (1,11) }
print(dict_v2)
'''

'''
#crear diccionario con lista de paises

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
    
print(population)

#con Dict comprehesion
population_v2 = {country:random.randint(1, 100) for country in countries}
print(population_v2)
'''

#Con dos listas iterar un diccionario

names = ['nico','zule','santi']
ages = [22, 27, 23]

print(list(zip(names,ages))) #La función zip une dos listas y con list al momento de imprimir, lo muestro en formato lista con tuplas adentro

dict_pna = {name:age for (name, age) in zip(names, ages)}
print(dict_pna)