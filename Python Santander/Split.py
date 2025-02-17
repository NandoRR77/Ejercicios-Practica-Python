'''
Separar una cadena de caracteres de acuerdo a un caracter definido
'''

a = '1;Fernando Ramirez;42;15/05/1983'

print(a)

a_split = str.split(a,";")

print(a_split)
print(type(a_split))


