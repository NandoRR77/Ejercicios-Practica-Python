'''
Ejercicio 1Permalink

Escribe un programa python que pida un número por teclado y que cree un diccionario 
cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los 
cuadrados de las claves
'''

num = int(input('Ingrese un número: '))
cuadrados = {}

#forma tradicional
for i in range(1,num+1):
    cuadrados[i] = i ** 2
print(cuadrados)

#con list comprehesion
cuadrados_v2 = {i:i**2 for i in range(1,num+1)}
print(cuadrados_v2)