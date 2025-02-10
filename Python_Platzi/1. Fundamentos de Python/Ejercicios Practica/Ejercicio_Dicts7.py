'''
Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenando con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
'''

persona = {}
continuar = True

while continuar:
    key = input('Que dato quiere ingresar/')
    value = input(key + ': ')
    persona[key] = value
    print(persona)
    continuar = input('Desea agregar mas información Si//No?: ')
