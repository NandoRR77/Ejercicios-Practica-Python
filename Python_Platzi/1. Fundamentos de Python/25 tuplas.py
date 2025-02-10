numbers = (1,2,3,4,5) #Las tuplas se identifican con () y son inmutables
strings = ('nando', 'cami', 'cris', 'juan', 'cris')

print(numbers)
print(type(numbers))

print(strings)
print(type(strings))

print(numbers[0]) #imprimir la posición 0
print(strings[3]) #imprimir la posición 3

print(strings.index('nando')) #buscar en una tupla
print(strings.count('cris')) #contar elementos en una tupla

#Convertir una tupla a una lista
my_list = list(strings)

my_list.append('Batman')
print(my_list)
print(type(my_list))

my_tuple = tuple(my_list)

print(type(my_tuple))
print(my_tuple)

