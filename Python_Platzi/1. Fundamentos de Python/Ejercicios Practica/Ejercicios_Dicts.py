'''
Ejercicios de Diccionarios
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y 
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('Por favor ingrese la divisa: \n')

if divisa in divisas:
    print(f'El símbolo de la divisa ingresada es: {divisas[divisa]}')
else:
    print(f'La divisa {divisa} no existe')
    print(f'Las divisas existentes son: {divisas}')
