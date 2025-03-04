'''
1. Escriba un programa Python para crear una función lambda que sume 15 a un número dado que se 
pasa como argumento, y también cree una función lambda que multiplique el argumento x por el 
argumento y e imprima el resultado.
Ejemplo de salida:
25
48
'''

suma = lambda x : x + 15
print(suma(10))


multiplica = lambda x,y : x * y
print(multiplica(6,8))
