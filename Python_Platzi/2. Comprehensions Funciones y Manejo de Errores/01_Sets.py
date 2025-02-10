set_countries = {'colombia', 'mexico' , 'bolivia'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,3,443}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola') #Conjunto creado a partir de un string
print(set_from_string) # de cada caracter, hace un elemento

set_from_tuple = set(('abc', 'cbd', 'thc', 'abc'))
print(set_from_tuple)

#set from numbers
numbers = [1,1,2,4,5,4,3,1]
set_numbers_2 = set(numbers)
print(set_numbers_2)

#transformar set a lista
unique_numbers = list(set_numbers_2)
print('Set to list')
print(unique_numbers)