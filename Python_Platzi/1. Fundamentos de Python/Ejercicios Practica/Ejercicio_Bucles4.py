'''
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
'''

num = int(input('Por favor ingrese un número: '))

for i in range(num,-1,-1):
    print(i, end=',')