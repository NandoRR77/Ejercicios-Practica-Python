'''
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono 
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
'''

person = {}
name = input('Por favor ingrese su nombre: \n')
age = input('Por favor ingrese su edad: \n')
address = input('Por favor ingrese su direccion: \n')
tel = input('Por favor ingrese su teléfono: \n')

person['name'] = name
person['age'] = age
person['address'] = address
person['tel'] = tel
print(f'{person['name']} tiene {person['age']} años, vive en {person['address']} y su número de teléfono es {person['tel']}')