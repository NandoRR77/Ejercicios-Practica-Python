'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

numbers = []

for i in range(6):
    numbers.append(int(input('Ingrese un número del 1 al 49: \n')))
    numbers.sort()
print('Los números ganadores son: ' , numbers)

