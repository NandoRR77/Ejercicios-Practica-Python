'''
Día 5 – Bucles for y while

- Imprime los números del 1 al 10 usando un for.

- Imprime la tabla de multiplicar de un número ingresado por el usuario.

- Suma los números del 1 al 100 con un while
'''

#Imprime los números del 1 al 10 usando un for
print('#Imprime los números del 1 al 10 usando un for')

numeros = list(map(lambda i : print(i), range(1,11)))

print('****************************************************\n')


#Imprime la tabla de multiplicar de un número ingresado por el usuario
print('#Imprime la tabla de multiplicar de un número ingresado por el usuario')

num_usuario = int(input('Ingrese un número del 1 al 10 => '))

for i in range(1,11):
    resultado = i * num_usuario
    print(f'{num_usuario} X {i} = {resultado}')

print('****************************************************\n')

#Suma los números del 1 al 100 con un while
print('#Suma los números del 1 al 100 con un while')

suma = 0
i = 1
while i <= 100:
    suma = suma + i
    i += 1
print(f'La suma de los números del 1 al 100 es {suma}')

print('****************************************************\n')