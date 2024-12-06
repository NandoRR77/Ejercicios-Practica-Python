person = {
    'name': 'Fernando',
    'last_name': 'Ramirez',
    'langs': ['Python', 'JavaScript'],
    'age': 99
}

print(person)

person['name'] = 'Jaiver' #Cambiar el valor de una llave
print(person)

person ['age'] -= 63 #Puedo hacer cálculos con el valor de la clave age porque es número
print(person)

person['langs'].append('Java') #Agregar un elemento al valor que como es una lista, se hase con append()
print(person)

del person['last_name'] #Eliminar par clave:valor 'last_name'
print(person)

person.pop('age') #Eliminar para clave:valor 'age', obligatoriamente se tiene que indicar cual
print(person)

print('\n\nConocer los items de un diccionario:')
print(person.items()) #Devuelve listas en pares de tuplas

print('\nConocer las keys de un diccionario:')
print(person.keys()) #Devuelve listas con atributos

print('\nConocer los values de un diccionario:')
print(person.values()) #Devuelve listas con atributos


