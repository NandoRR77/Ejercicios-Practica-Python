'''
Ejercicio 3
Escribir un algoritmo que pida un número entero positivo y devuelva su factorial.
'''

num = int(input('Por favor ingrese un número entero: '))
factorial = 1
for i in range(num,1,-1):
    factorial *= i 
print('El factorial de ' , num , 'es = ' , factorial)