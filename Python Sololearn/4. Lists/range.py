''' con range(10) se generan 10 numeros de 0 a 9, con incrementos de 1 en 1
Para generar el rango como una lista, debemos convertirlo explícitamente en una lista, usando la función list().
si en el rango se pone 1 solo argumento, produce un rango de 0 hasta ese número'''
print("Ejemplo 1 - range(10)")
numbers = list(range(10))
print(numbers)

'''si se ponen 2 argumentos, se produce un rango desde el primer elemento hasta el segundo'''
print("Ejemplo 2 argumentos - range(3,8)")
numbers = list(range(3, 8))
print(numbers)

'''si se ponen 3 argumentos, se produce un rango desde el primer elemento hasta el segundo, el tercer argumento indica el incremento'''
print("Ejemplo 3 argumentos - range(5, 20, 2)")
numbers = list(range(5, 20, 2))
print(numbers)

'''si se ponen 3 argumentos, se produce un rango desde el primer elemento hasta el segundo, el tercer argumento indica el o decremento'''
print("Ejemplo 3 argumentos - range(7, 3, -1)")
x = list(range(7, 3, -1))
print(x)

'''You can use ranges in for loops, without the need to convert them into lists. It's commonly used to repeat some code a certain number of times. Like this'''
for i in range(5):
  print("hello!")