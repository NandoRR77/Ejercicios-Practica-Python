'''
Día 2 – Más variables y operaciones

- Convierte grados Celsius a Fahrenheit.

- Calcula el perímetro de un círculo dado su radio.

- Pide al usuario dos números y muestra cuál es mayor.
'''


import math

#Ejercicio convierte grados Celsius a Fahrenheit
# F = 0 C° * (9/5) + 32)
print('\n#Ejercicio convierte grados Celsius a Fahrenheit')

celsius = float(input('Ingrese los grados C° a convertir => '))
fahrenheit = (celsius * (9/5) + 32)
print(f'Grados Celsius => {celsius}C°')
print(f'Grados Fahrenheit => {fahrenheit}F°')

print('\n****************************************************\n')


#Ejercicio Calcula el perímetro de un círculo dado su radio
#Perimetro = 2πr
print('#Calcula el perímetro de un círculo dado su radio')

radio = float(input('Ingrese el radio => '))
perimetro = round((2*math.pi*radio),2)
print(f'Radio ingresado => {radio}')
print(f'El perímetro es  => {perimetro}')

print('\n****************************************************\n')


#Ejercicio Pide al usuario dos números y muestra cuál es mayor
#Perimetro = 2πr
print('#Calcula el mayor de dos números')

num1 = int(input('Ingrese el número 1 => '))
num2 = int(input('Ingrese el número 2 => '))

#Con función
def num_mayor(num1, num2):
    if num1 == num2:
        return print(f'Los números ingresados son iguales')
    elif num1 > num2: 
        return print(f'El número {num1} es mayor que el número {num2}')
    else: 
        return print(f'El número {num2} es mayor que el número {num1}')

num_mayor(num1, num2)

print('\n****************************************************\n')



