import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

population_v2 = {country:random.randint(1, 100) for country in countries}
print(population_v2)

#Filtrar los paises cuya población sea mayor a 20

result = { country:population for (country, population) in population_v2.items() if population > 20 }
print(result)


#A partir de un string, generar un diccionario con las vocales

text = 'Hola, soy Nandorea77'
unique = {c:c.upper() for c in text if c in 'aeiou'}
print(unique)