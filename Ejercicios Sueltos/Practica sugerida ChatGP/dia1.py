'''
Día 1 – Variables y operadores
- Declara dos variables numéricas y muestra su suma, resta, multiplicación y división.
- Pide al usuario su nombre y muéstralo en pantalla con un saludo.
- Calcula el área de un triángulo (base * altura / 2).
'''

#Ejercicio variables
print('#Ejercicio variables')
num_1 = 3
num_2 = 4

print(f'Suma: {num_1 + num_2}')
print(f'Resta: {num_1 - num_2}')
print(f'Multiplicación: {num_1 * num_2}')
print(f'División: {num_1 / num_2}')

print('///'*10)


#Ejercicio nombre usuario y saludo
print('#Ejercicio nombre usuario y saludo')
nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}, recibe un cordial saludo')

print('///'*10)

#Ejercicio área del triángulo
print('#Ejercicio área del triángulo')
base = float(input('La base del triángulo: '))
altura = float(input('La altura del triángulo: '))
area = base * altura

print(f'El área del triángulo de base {base} y altura {altura} es: {area}')

print('///'*10)