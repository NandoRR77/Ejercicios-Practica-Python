'''
Día 3 – Condicionales básicos

- Escribe un programa que diga si un número es par o impar.

- Pide la edad al usuario y muestra si es mayor o menor de edad.

- Dado un número, indica si es positivo, negativo o cero
'''

#número es par o impar
print('#Número es par o impar')

num = int(input('Ingrese el número => '))
par_impar = (lambda num : "es par" if num % 2 == 0 else "es impar")
print(f'El número es => {par_impar(num)}')

print('****************************************************\n')


#Pide la edad al usuario y muestra si es mayor o menor de edad.
print('#Mayor o menor de edad')

edad = int(input('Ingrese su edad = > '))

calcula_edad = lambda edad: 'Mayor de edad' if edad >= 18 else 'Menor de edad'

print(f'Según la edad ingresada, la persona es: {calcula_edad(edad)}')


print('****************************************************\n')


#Dado un número, indica si es positivo, negativo o cero
print('#Indica si es positivo, negativo o cero')

num1 = int(input('Ingrese un número entero => '))

valida_num = lambda num1: 'Cero' if num1 == 0 else ('Negativo' if num1 <= 0 else 'Positivo')

print(f'El número ingresado es: {valida_num(num1)}')

print('****************************************************\n')